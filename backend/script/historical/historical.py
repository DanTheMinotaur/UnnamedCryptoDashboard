import asyncio
from datetime import datetime, timedelta, date
from os.path import abspath
from pathlib import Path
from typing import Dict, List

from tortoise import Tortoise, run_async, functions
import aiohttp
from models import Crypto, Historical

SQLITE_DEFAULT_PATH = f'sqlite://{Path(abspath(__file__)).parent.resolve().joinpath("historical.sqlite")}'


async def init_db(db_string: str = SQLITE_DEFAULT_PATH):
    await Tortoise.init(
        db_url=db_string,
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

# 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listings/historical?date=2020-02-05&limit=3000&start=1'


class HistoricalDataCollector:
    def __init__(self):
        self.cryptos: Dict[str, Crypto] = {}
        self._new_cryptos: List[Crypto] = []
        self.base_url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listings/historical'

    # Origin Date for coinmarketcap
    START_DATE = datetime.strptime('2013-04-28', '%Y-%m-%d')

    async def get_last_scraped_date(self) -> date:
        last_date = await Historical.annotate(max_col=functions.Max('date')).first()
        if last_date.date:
            return last_date.date
        return HistoricalDataCollector.START_DATE.date()

    async def load_existing_cryptos(self) -> Dict[str, Crypto]:
        _all = await Crypto.all()
        self.cryptos = {c.symbol: c for c in _all}
        return self.cryptos

    async def create_new_crypto_entries(self):
        if len(self._new_cryptos) == 0:
            return
        await Crypto.bulk_create(self._new_cryptos, ignore_conflicts=True)
        # Using bulk_create doesn't register _saved_in_db field, need to reload data to continue using bulk_create
        await self.load_existing_cryptos()
        self._new_cryptos = []

    def parse_coinmarketcap_response(self, resp: dict) -> List[Dict]:
        data = resp['data']
        parsed_history: List[Dict] = []
        for entry in data:
            symbol = entry['symbol']
            if symbol not in self.cryptos:
                self._new_cryptos.append(Crypto(name=entry['name'], symbol=symbol))

            dollar_value = float(entry['quotes'][0]['price'])
            parsed_history.append({
                "crypto": symbol,
                "dollar_value": dollar_value
            })
        return parsed_history

    async def scrape_historical_by_date(self, _date: date, session: aiohttp.ClientSession):
        date_str = _date.strftime('%Y-%m-%d')
        print(f"Pull data for {date_str}")
        url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listings/historical?date={date_str}&limit=30000&start=1"

        async with session.get(url) as resp:
            parsed_history = self.parse_coinmarketcap_response(await resp.json())

        await self.create_new_crypto_entries()

        to_create = []
        for h in parsed_history:
            h.update({
                "crypto": self.cryptos[h['crypto']],
                "date": _date
            })
            to_create.append(
                Historical(**h)
            )

        await Historical.bulk_create(to_create, ignore_conflicts=True)

    async def scrape_dates(self, dates: List[date], session: aiohttp.ClientSession):
        coro = [self.scrape_historical_by_date(d, session) for d in dates]
        await asyncio.gather(*coro)

    async def scrape_all(self, concurrency: int = 10):
        from_date = await self.get_last_scraped_date()
        todays_date = datetime.now().date()

        async with aiohttp.ClientSession() as session:
            while from_date < todays_date:
                dates = [from_date + timedelta(days=d) for d in range(concurrency)]
                await self.scrape_dates(dates, session)
                from_date += timedelta(days=concurrency)


if __name__ == "__main__":

    async def run():
        await init_db()
        dc = HistoricalDataCollector()
        await dc.scrape_all()



    run_async(run())

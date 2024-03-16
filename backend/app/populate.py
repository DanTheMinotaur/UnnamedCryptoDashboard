from tortoise import run_async
from .db.models.crypto import Crypto
from .datasource.coincap import CoinCapAPI
from .db.init_db import init_db, models_append


async def cryptos(coincap: CoinCapAPI, asset_limit: int = 2000):
    asset_count = 0
    _break = False

    while True:
        assets = await coincap.get_assets(limit=asset_limit, offset=asset_count)
        if len(assets) == 0:
            break
        models = [Crypto(name=a['name'], symbol=a['symbol']) for a in assets]
        await Crypto.bulk_create(models, ignore_conflicts=True)
        asset_count += len(assets)


if __name__ == "__main__":
    c = CoinCapAPI()
    run_async(init_db(models_append('app.db')))
    run_async(cryptos(c))
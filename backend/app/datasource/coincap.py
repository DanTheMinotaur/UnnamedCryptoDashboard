import aiohttp
from datetime import datetime

class CoinCapAPI:
    class CoinCapAPIException(Exception):
        pass

    def __init__(self, auth_token: str = None, gzip: bool = True):
        self.base_url = 'https://api.coincap.io/v2'
        self.headers = {}
        if gzip:
            self.set_header('Accept-Encoding', 'gzip')
        if auth_token:
            self.set_header('Authorization', f'Bearer {auth_token}')

    HISTORY_INTERVALS = {'m1', 'm5', 'm15', 'm30', 'h1', 'h2', 'h6', 'h12', 'd1'}

    def set_header(self, name: str, value: str) -> None:
        self.headers[name] = value

    async def _get_request(self, endpoint: str, params: dict = None) -> dict:
        if params is None:
            params = {}
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(f'{self.base_url}/{endpoint}', params=params) as response:
                resp = await response.json()
                return resp['data']

    async def get_assets(self, limit: int = 10, offset: int = 0):
        return await self._get_request('assets', params={'limit': limit, 'offset': offset})

    async def get_asset_by_id(self, asset_id: str):
        return await self._get_request(f'assets/{asset_id}')

    async def get_asset_history(self, asset_id: str, interval: str = 'h1', start: datetime = None, end: datetime = None):
        if interval not in CoinCapAPI.HISTORY_INTERVALS:
            raise CoinCapAPI.CoinCapAPIException(f"'{interval}' is invalid, valid options are {CoinCapAPI.HISTORY_INTERVALS}")
        params = {'interval': interval}
        if start:
            params['start'] = start.strftime('%s')
        if end:
            params['end'] = end.strftime('%s')
        return await self._get_request(f'assets/{asset_id}/history', params=params)

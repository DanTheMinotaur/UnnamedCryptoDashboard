import pytest
import json

from app.populate import cryptos
from app.db.models.crypto import Crypto


def load_test_assets():
    asset_file = './.data/assets_coincap.json'

    with open(asset_file, 'r') as f:
        data = json.loads(f.read())
    return data['data']


asset_data = load_test_assets()


@pytest.mark.asyncio
async def test_cryptos(mocker, db_conn):
    asset_limit: int = 2
    m1 = asset_data[:asset_limit]
    m2 = asset_data[asset_limit:asset_limit * 2]

    mock_response = mocker.Mock(side_effect=[m1, m2, []])

    class MockCoinCap:
        async def get_assets(self, *_args, **_kwargs):
            return mock_response()

    await cryptos(MockCoinCap(), asset_limit)

    assert len(await Crypto.all()) == 4

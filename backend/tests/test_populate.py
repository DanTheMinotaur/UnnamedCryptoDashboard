import pytest

from app.populate import populate_cryptos
from app.db.models.crypto import Crypto
from app.datasource.abs import DataSource


@pytest.mark.asyncio
async def test_cryptos(mocker, db_conn, helpers):
    asset_limit: int = 2
    asset_data = helpers.load_test_json('assets_coincap.json')
    m1 = asset_data[:asset_limit]
    m2 = asset_data[asset_limit:asset_limit * 2]

    mock_response = mocker.Mock(side_effect=[m1, m2, []])

    class MockCoinCap(DataSource):
        SOURCE = 'MOCK'
        LOOKUP_KEY = 'id'

        async def get_assets(self, *_args, **_kwargs):
            return mock_response()

    await populate_cryptos(MockCoinCap(), asset_limit)

    assert len(await Crypto.all()) == 4

import pytest
from app.datasource.coincap import CoinCapAPI
from datetime import datetime

"""
`mocker` comes from pytest-mock package
"""


def test_request_headers():
    auth_code = 'ABC'
    c = CoinCapAPI(auth_code)

    assert 'Accept-Encoding' in c.headers
    assert c.headers['Accept-Encoding'] == 'gzip'
    assert 'Authorization' in c.headers
    assert c.headers['Authorization'] == f'Bearer {auth_code}'

    c = CoinCapAPI(gzip=False)

    assert c.headers == {}


coincap = CoinCapAPI()


@pytest.mark.asyncio
async def test_get_assets_with_header(mocker):
    mock = mocker.patch('aiohttp.ClientSession.get')

    params = {"limit": 10, "offset": 1}

    await coincap.get_assets(**params)

    mock.assert_called_once_with(
        f'{coincap.base_url}/assets', params=params
    )


@pytest.mark.asyncio
async def test_get_asset_by_id(mocker):
    mock = mocker.patch('aiohttp.ClientSession.get')

    asset_id = 'abc'

    await coincap.get_asset_by_id(asset_id)

    mock.assert_called_once_with(
        f'{coincap.base_url}/assets/{asset_id}', params={}
    )


@pytest.mark.asyncio
async def test_get_asset_history(mocker):
    mock = mocker.patch('aiohttp.ClientSession.get')

    asset_id = 'abc'
    expected_url = f'{coincap.base_url}/assets/{asset_id}/history'

    await coincap.get_asset_history(asset_id)

    mock.assert_called_once_with(expected_url, params={"interval": "h1"})

    mock = mocker.patch('aiohttp.ClientSession.get')

    current_dt = datetime.now()

    await coincap.get_asset_history(asset_id, interval='m15', start=current_dt, end=current_dt)
    mock.assert_called_once_with(expected_url, params={
        "interval": "m15",
        "start": current_dt.strftime('%s'),
        "end": current_dt.strftime('%s')
    })


@pytest.mark.asyncio
async def test_get_asset_history_interval_exception():
    invalid_interval = 'abc'

    with pytest.raises(CoinCapAPI.CoinCapAPIException) as ex:
        await coincap.get_asset_history('abc', invalid_interval)

        assert f"'abc' is invalid, valid options are {CoinCapAPI.HISTORY_INTERVALS}" in str(ex)

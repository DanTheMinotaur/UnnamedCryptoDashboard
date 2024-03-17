import pytest
from app.db.models.crypto import Crypto
from app.db.models.holdings import Holdings
from app.db.models.price_history import CryptoPriceHistory
from tortoise.exceptions import IntegrityError


@pytest.mark.asyncio
async def test_crypto_model(db_conn):
    meta = {"test": "data"}

    c1 = await Crypto.create(name='Bitcoin', symbol='BTC', meta=meta)
    assert c1 is not None
    assert c1.meta == meta

    c2 = await Crypto.create(name='Ethereum', symbol='ETH')
    assert c2 is not None

    _all = await Crypto.all()
    assert len(_all) == 2

    search = await Crypto.filter(symbol='ETH')
    assert len(search) == 1
    assert search[0].name == 'Ethereum'

    with pytest.raises(IntegrityError) as ex:
        await Crypto.create(name='Bitcoin', symbol='BTC')
        assert 'UNIQUE constraint failed' in ex


@pytest.mark.asyncio
async def test_holdings_model(db_conn):
    btc = await Crypto.create(name='Bitcoin', symbol='BTC')
    u1 = 0.12
    u2 = 0.000345
    await Holdings.create(units=u1, crypto=btc)
    await Holdings.create(units=u2, crypto=btc)

    _all = Holdings.all()
    assert len(await _all) == 2

# @pytest.mark.asyncio
# async def test_price_history_model():
#     ph = await CryptoPriceHistory(unit_value=)

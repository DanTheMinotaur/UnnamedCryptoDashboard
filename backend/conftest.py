import pytest
import asyncio
from app.db.init_db import init_db, models_append
from tortoise import Tortoise


@pytest.fixture
def db_conn():
    def run(func):
        asyncio.get_event_loop().run_until_complete(func)

    run(init_db(models_append('app.db'), 'sqlite://:memory:'))
    yield
    run(Tortoise.close_connections())

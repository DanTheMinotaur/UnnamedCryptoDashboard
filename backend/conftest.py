from os.path import abspath

import pytest
import asyncio
from app.db.init_db import init_db, models_append
from tortoise import Tortoise
from pathlib import Path
import json


@pytest.fixture
def db_conn():
    def run(func):
        asyncio.get_event_loop().run_until_complete(func)

    sqlite_mem = 'sqlite://:memory:'
    run(init_db(models_append('app.db'), sqlite_mem))
    yield
    run(Tortoise.close_connections())


class Helpers:
    HELPER_DATA_DIR = Path(abspath(__file__)).parent.joinpath('tests/.data')
    LOADED_DATA = {}

    @staticmethod
    def load_test_json(filename: str) -> dict:
        json_file = str(Helpers.HELPER_DATA_DIR.joinpath(filename))
        if json_file in Helpers.LOADED_DATA:
            return Helpers.LOADED_DATA[json_file]

        with open(json_file, 'r') as f:
            data = json.loads(f.read())
        Helpers.LOADED_DATA[json_file] = data['data']
        return Helpers.LOADED_DATA[json_file]


@pytest.fixture(scope='session')
def helpers():
    return Helpers

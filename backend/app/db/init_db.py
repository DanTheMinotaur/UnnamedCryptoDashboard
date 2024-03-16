from tortoise import Tortoise, run_async
from pathlib import Path
from os.path import abspath

MODELS = (
    'models.crypto',
    'models.holdings',
    'models.price_history',
)

SQLITE_DEFAULT_PATH = f'sqlite://{Path(abspath(__file__)).parent.parent.parent.resolve().joinpath("db.sqlite3")}'


def models_append(module_parent: str) -> tuple:
    return tuple([f'{module_parent}.{m}' for m in MODELS])


async def init_db(models: list or tuple = MODELS, db_string: str = SQLITE_DEFAULT_PATH):
    await Tortoise.init(
        db_url=db_string,
        modules={'models': models}
    )
    await Tortoise.generate_schemas()


if __name__ == "__main__":
    run_async(init_db(MODELS, SQLITE_DEFAULT_PATH))

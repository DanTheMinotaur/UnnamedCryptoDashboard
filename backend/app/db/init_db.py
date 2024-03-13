from tortoise import Tortoise, run_async


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': [
            'models.crypto',
            'models.holdings',
            'models.price_history'
        ]}
    )
    await Tortoise.generate_schemas()

if __name__ == "__main__":
    run_async(init())

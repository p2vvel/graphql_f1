from tortoise import Tortoise, run_async

from app.config import config


async def init():
    # Here we create a SQLite DB using file "db.sqlite3"
    #  also specify the app name of "models"
    #  which contain models from "app.models"
    await Tortoise.init(
        db_url=f"mysql://{config.mysql_user}:{config.mysql_password}@{config.mysql_host}:{config.mysql_port}/{config.mysql_db}",
        modules={"models": ["app.db.models"]},
    )

    # Generate the schema
    await Tortoise.generate_schemas()


# run_async is a helper function to run simple async Tortoise scripts.
run_async(init())

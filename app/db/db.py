from tortoise import Tortoise

from app.config import config


async def initialize_db() -> None:
    connection_string = "mysql://{user}:{password}@{host}:{port}/{db}".format(
        user=config.mysql_user,
        password=config.mysql_password,
        host=config.mysql_host,
        port=config.mysql_port,
        db=config.mysql_db,
    )
    await Tortoise.init(
        db_url=connection_string,
        modules={"models": ["app.db.models"]},
    )

    await Tortoise.generate_schemas()


async def close_db() -> None:
    await Tortoise.close_connections()

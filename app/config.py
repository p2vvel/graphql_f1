from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mysql_host: str = "127.0.0.1"
    mysql_port: int = 3306
    mysql_user: str = "f1user"
    mysql_password: str = "f1password"
    mysql_db: str = "f1db"


config = Config()

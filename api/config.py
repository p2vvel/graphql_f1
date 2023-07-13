from pydantic.config import BaseSettings


class Settings(BaseSettings):
    db_url: str = "mysql+pymysql://root:1234@localhost:3306/f1?charset=utf8"

    class Config:
        env_file = ".env"

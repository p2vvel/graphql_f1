from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper
from functools import lru_cache


@lru_cache      # use same mapper in all modules
def get_mapper() -> StrawberrySQLAlchemyMapper:
    mapper = StrawberrySQLAlchemyMapper()
    return mapper

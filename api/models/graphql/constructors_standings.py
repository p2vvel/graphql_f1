from .base import mapper
from .. import sql


@mapper.type(sql.ConstructorStanding)
class ConstructorStanding:
    pass

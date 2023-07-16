from .base import mapper
from .. import sql


@mapper.type(sql.ConstructorResult)
class ConstructorResult:
    pass

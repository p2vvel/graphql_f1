from .base import mapper
from .. import sql


@mapper.type(sql.Result)
class Result:
    pass

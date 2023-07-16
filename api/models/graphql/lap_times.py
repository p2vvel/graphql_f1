from .base import mapper
from .. import sql


@mapper.type(sql.LapTime)
class LapTime:
    pass

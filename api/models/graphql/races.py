from .base import mapper
from .. import sql


@mapper.type(sql.Race)
class Race:
    pass

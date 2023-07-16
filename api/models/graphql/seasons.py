from .base import mapper
from .. import sql


@mapper.type(sql.Season)
class Season:
    pass

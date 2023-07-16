from .base import mapper
from .. import sql


@mapper.type(sql.Qualifying)
class Qualifying:
    pass

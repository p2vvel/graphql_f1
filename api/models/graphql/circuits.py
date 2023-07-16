from .base import mapper
from .. import sql


@mapper.type(sql.Circuit)
class Circuit:
    pass

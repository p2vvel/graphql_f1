from .base import mapper
from .. import sql


@mapper.type(sql.PitStops)
class PitStops:
    pass

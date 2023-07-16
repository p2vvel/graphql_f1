from .. import sql
from .base import get_mapper


mapper = get_mapper()


@mapper.type(sql.PitStops)
class PitStops:
    pass

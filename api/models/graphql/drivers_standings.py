from .. import sql
from .base import get_mapper


mapper = get_mapper()


@mapper.type(sql.DriverStanding)
class DriverStanding:
    pass

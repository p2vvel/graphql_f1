from .base import mapper
from .. import sql


@mapper.type(sql.DriverStanding)
class DriverStanding:
    pass

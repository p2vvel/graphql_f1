from .base import mapper
from .. import sql


@mapper.type(sql.Driver)
class Driver:
    pass

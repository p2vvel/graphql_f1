from .base import mapper
from .. import sql


@mapper.type(sql.Status)
class Status:
    pass

from .base import mapper
from .. import sql


@mapper.type(sql.SprintResult)
class SprintResult:
    pass

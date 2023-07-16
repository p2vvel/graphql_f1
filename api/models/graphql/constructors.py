from .base import mapper
from .. import sql


@mapper.type(sql.Constructor)
class Constructor:
    pass

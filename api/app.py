import strawberry

from .models.graphql.base import get_mapper
from .db import SessionLocal
from sqlalchemy import select
from .models import sql, graphql


mapper = get_mapper()
db = SessionLocal()


def resolve_drivers(root):
    data = db.scalars(select(sql.Driver)).all()
    return data


@strawberry.type
class Query:
    drivers: list[graphql.Driver] = strawberry.field(resolver=resolve_drivers, )


mapper.finalize()
additional_types = list(mapper.mapped_types.values())
schema = strawberry.Schema(
    query=Query,
    types=additional_types,
)

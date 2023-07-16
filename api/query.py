from .models.graphql.base import get_mapper
from .db import SessionLocal
from sqlalchemy import select
from .models import sql, graphql
import strawberry


mapper = get_mapper()
db = SessionLocal()


def resolve_drivers(root):
    data = db.scalars(select(sql.Driver)).all()
    return data


@strawberry.type
class Query:
    drivers: list[graphql.Dr] = strawberry.field(resolver=resolve_drivers, )

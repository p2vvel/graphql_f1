import strawberry

from api.db import SessionLocal
from sqlalchemy import select
from api.models import sql, graphql


# mapper = get_mapper()
db = SessionLocal()


def resolve_drivers(root):
    data = db.scalars(select(sql.Driver)).all()
    return data


@strawberry.type
class DriversQuery:
    drivers: list[graphql.Driver] = strawberry.field(resolver=resolve_drivers)

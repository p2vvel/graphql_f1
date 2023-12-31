# flake8: noqa: E127
import strawberry
from api.db import SessionLocal
from sqlalchemy import select
from api.models import sql, graphql
from .utils import create_filters


db = SessionLocal()


@strawberry.type
class DriversQuery:
    @strawberry.field
    def drivers(self, 
                id: int | None = None, 
                forename: str | None = None, 
                surname: str | None = None, 
                nationality: str | None = None,
                driver_ref: str | None = None,) -> list[graphql.Driver]:
        filters = create_filters(sql.Driver, ("id", "forename", "surname", "nationality", "driver_ref"), locals())

        stmt = select(sql.Driver).where(*filters)
        data = db.scalars(stmt).all()

        return data

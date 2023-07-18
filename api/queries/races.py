# flake8: noqa: E127
import strawberry
from api.db import SessionLocal
from sqlalchemy import select
from api.models import sql, graphql
from .utils import create_filters


db = SessionLocal()


@strawberry.type
class RacesQuery:
    @strawberry.field
    def races(self,
                id: int | None = None,
                year: int | None = None,
                round: int | None = None,
                name: str | None = None,
                ) -> list[graphql.Race]:
        filters = create_filters(sql.Race, ("id", "year", "round", "name"), locals())

        stmt = select(sql.Race).where(*filters)
        data = db.scalars(stmt).all()

        return data

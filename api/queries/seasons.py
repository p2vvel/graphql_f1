# flake8: noqa: E127
import strawberry
from api.db import SessionLocal
from sqlalchemy import select
from api.models import sql, graphql
from .utils import create_filters


db = SessionLocal()


@strawberry.type
class SeasonsQuery:
    @strawberry.field
    def seasons(self, 
                year: int | None = None, 
                ) -> list[graphql.Season]:
        filters = create_filters(sql.Season, ("year",), locals())

        stmt = select(sql.Season).where(*filters)
        data = db.scalars(stmt).all()

        return data

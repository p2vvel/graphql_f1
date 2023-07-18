# flake8: noqa: E127
import strawberry
from api.db import SessionLocal
from sqlalchemy import select
from api.models import sql, graphql
from .utils import create_filters


db = SessionLocal()


@strawberry.type
class ConstructorsQuery:
    @strawberry.field
    def constructors(self, 
                id: int | None = None, 
                name: str | None = None, 
                nationality: str | None = None,
                constructor_ref: str | None = None) -> list[graphql.Constructor]:
        filters = create_filters(sql.Constructor, ("id", "name", "nationality", "constructor_ref"), locals())

        stmt = select(sql.Constructor).where(*filters)
        data = db.scalars(stmt).all()

        return data

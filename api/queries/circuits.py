# flake8: noqa: E127
import strawberry
from api.db import SessionLocal
from sqlalchemy import select
from api.models import sql, graphql
from .utils import create_filters


db = SessionLocal()


@strawberry.type
class CircuitsQuery:
    @strawberry.field
    def circuits(self, id: int | None = None, 
                name: str | None = None, 
                country: str | None = None,
                location: str | None = None,
                circuit_ref: str | None = None,
                ) -> list[graphql.Circuit]:
        filters = create_filters(sql.Circuit, ("id", "name", "country", "location", "circuit_ref"), locals())

        stmt = select(sql.Circuit).where(*filters)
        data = db.scalars(stmt).all()

        return data

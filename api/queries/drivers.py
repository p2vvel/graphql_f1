import strawberry

from api.db import SessionLocal
from sqlalchemy import select, and_
from api.models import sql, graphql


# mapper = get_mapper()
db = SessionLocal()


# def resolve_drivers(root, info, 
#                     id: int | None = None,
#                     forename: str | None = None,
#                     surname: str | None = None,
#                     nationality: str | None = None,
#                     ):
    
#     data = db.scalars(select(sql.Driver)).all()
#     return data


@strawberry.type
class DriversQuery:
    # drivers: list[graphql.Driver] = strawberry.field(resolver=resolve_drivers)
    @strawberry.field
    def drivers(self, id: int | None = None,
                    forename: str | None = None,
                    surname: str | None = None,
                    nationality: str | None = None,) -> list[graphql.Driver]:
        locals_ = locals()
        check_field = {k: locals_.get(k) for k in ("id", "forename", "surname", "nationality") if locals_.get(k) is not None}
        conditions = [getattr(sql.Driver, par).__eq__(val) for par, val in check_field.items()]

        stmt = select(sql.Driver).where(*conditions)
        data = db.scalars(stmt).all()

        return data

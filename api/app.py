import strawberry
from strawberry.tools import merge_types
from .models.graphql.base import get_mapper
from .db import SessionLocal
from api import queries

mapper = get_mapper()
db = SessionLocal()


mapper.finalize()
additional_types = list(mapper.mapped_types.values())
query = merge_types("api", (
    queries.DriversQuery,
    queries.ConstructorsQuery,
    queries.CircuitsQuery,
    queries.SeasonsQuery,
    queries.RacesQuery
))

schema = strawberry.Schema(
    query=query,
    types=additional_types,
)


if __name__ == "__main__":
    from sqlalchemy import select
    from .models import sql
    db = SessionLocal()
    import logging
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    stmt = select(sql.Season.year, sql.Season.last_round)
    data = db.execute(stmt).all()

    print(data)
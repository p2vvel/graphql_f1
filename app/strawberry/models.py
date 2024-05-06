import datetime

import strawberry


@strawberry.type
class Drivers:
    id: int
    ref: str
    number: int | None
    code: str | None
    forename: str
    surname: str
    dob: datetime.date | None
    nationality: str | None
    url: str


async def get_drivers():
    from app.db.models import Drivers

    return await Drivers.all()


@strawberry.type
class Query:
    drivers: list["Drivers"] = strawberry.field(resolver=get_drivers)

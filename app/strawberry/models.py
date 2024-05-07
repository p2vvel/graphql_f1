import datetime

import strawberry


@strawberry.type
class Drivers:
    id: int
    ref: strawberry.Private[str]  # hidden field
    number: int | None
    code: str | None
    forename: str
    surname: str
    date_of_birth: datetime.date | None
    nationality: str | None
    url: str

    # age: int = strawberry.field(resolver=age_resolver)
    @strawberry.field
    def age(self) -> int:
        timedelta = datetime.date.today() - self.date_of_birth
        return timedelta // datetime.timedelta(days=365.2425)


async def get_drivers():
    from app.db.models import Drivers

    return await Drivers.all()


@strawberry.type
class Query:
    drivers: list["Drivers"] = strawberry.field(resolver=get_drivers)

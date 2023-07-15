from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from datetime import date


class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(name="driverId", nullable=False, primary_key=True)
    driver_ref: Mapped[int] = mapped_column(name="driverRef", nullable=False)

    number: Mapped[int]
    code: Mapped[str]

    forename: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)

    dob: Mapped[date]
    nationality: Mapped[str]

    url: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __repr__(self):
        return f'<Driver: "{self.forename} {self.surname}">'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(Driver)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

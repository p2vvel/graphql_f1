from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from datetime import date


class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(name="driverId", nullable=False, primary_key=True)
    driver_ref: Mapped[str] = mapped_column(name="driverRef", nullable=False)

    number: Mapped[int | None]
    code: Mapped[str | None]

    forename: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)

    dob: Mapped[date | None]
    nationality: Mapped[str | None]

    url: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __repr__(self):
        return f'<Driver: "{self.forename} {self.surname}">'

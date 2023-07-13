from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Date
from .base import Base


class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(name="driverId", nullable=False, primary_key=True)
    driver_ref: Mapped[int] = mapped_column(name="driverRef", nullable=False)

    number: Mapped[int]
    code: Mapped[str]

    forename: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)

    dob: Mapped[Date]
    nationality: Mapped[str]

    url: Mapped[str] = mapped_column(nullable=False, unique=True)

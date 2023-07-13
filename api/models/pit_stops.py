from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Time
from .base import Base


class PitStops(Base):
    __tablename__ = "pitStops"

    race_id: Mapped[int] = mapped_column(name="raceId", primary_key=True, nullable=False)
    driver_id: Mapped[int] = mapped_column(name="driverId", primary_key=True, nullable=False)
    stop: Mapped[int] = mapped_column(nullable=False, primary_key=True)

    lap: Mapped[int] = mapped_column(nullable=False)
    time: Mapped[Time] = mapped_column(nullable=False)

    duration: Mapped[str]
    milliseconds: Mapped[int]

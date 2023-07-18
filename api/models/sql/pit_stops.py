from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base
from datetime import time as time_type


class PitStops(Base):
    __tablename__ = "pitStops"

    race_id: Mapped[int] = mapped_column(ForeignKey("races.raceId"), name="raceId", primary_key=True, nullable=False)       # noqa: E501
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.driverId"), name="driverId", primary_key=True, nullable=False)    # noqa: E501
    stop: Mapped[int] = mapped_column(nullable=False, primary_key=True)

    lap: Mapped[int] = mapped_column(nullable=False)
    time: Mapped[time_type] = mapped_column(nullable=False)

    duration: Mapped[str | None]
    milliseconds: Mapped[int | None]

    race: Mapped["Race"] = relationship()       # noqa: F821
    driver: Mapped["Driver"] = relationship()       # noqa: F821

    def __repr__(self):
        return f'<PitStop race={self.race_id} driver={self.driver_id} lap={self.lap}>'

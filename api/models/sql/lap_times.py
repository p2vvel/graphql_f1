from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class LapTime(Base):
    __tablename__ = "lapTimes"

    race_id: Mapped[int] = mapped_column(ForeignKey("races.raceId"), name="raceId", nullable=False, primary_key=True)   # noqa: E501
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.driverId"), name="driverId", nullable=False, primary_key=True)   # noqa: E501
    lap: Mapped[int] = mapped_column(nullable=False, primary_key=True)

    position: Mapped[int | None]
    time: Mapped[str | None]
    milliseconds: Mapped[int | None]

    driver: Mapped["Driver"] = relationship()               # noqa: F821
    race: Mapped["Race"] = relationship()                   # noqa: F821

    def __repr__(self):
        return f'<Laptime race={self.race_id} driver={self.driver_id} lap={self.lap}>'

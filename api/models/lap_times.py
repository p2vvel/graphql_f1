from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class LapTime(Base):
    __tablename__ = "lapTimes"

    race_id: Mapped[int] = mapped_column(name="raceId", nullable=False, primary_key=True)
    driver_id: Mapped[int] = mapped_column(name="driverId", nullable=False, primary_key=True)
    lap: Mapped[int] = mapped_column(nullable=False, primary_key=True)

    position: Mapped[int]
    time: Mapped[str]
    milliseconds: Mapped[int]

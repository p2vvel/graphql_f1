from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Result(Base):
    __tablename__ = "results"

    id: Mapped[int] = mapped_column(name="resultId", primary_key=True, nullable=False)
    race_id: Mapped[int] = mapped_column(name="raceId", nullable=False)
    driver_id: Mapped[int] = mapped_column(name="driverId", nullable=False)
    constructor_id: Mapped[int] = mapped_column(name="constructorId", nullable=False)

    number: Mapped[int] = mapped_column(nullable=False)
    grid: Mapped[int] = mapped_column(nullable=False)
    position: Mapped[int]
    position_text: Mapped[str] = mapped_column(name="positionText", nullable=False)
    position_order: Mapped[int] = mapped_column(name="positionOrder", nullable=False)

    points: Mapped[float] = mapped_column(nullable=False)
    laps: Mapped[int] = mapped_column(nullable=False)
    
    time: Mapped[str]
    milliseconds: Mapped[int]

    fastestLap: Mapped[int] = mapped_column(name="fastestLap")
    rank: Mapped[int]

    fastest_lap_time: Mapped[str] = mapped_column(name="fastestLapTime")
    fastest_lap_speed: Mapped[str] = mapped_column(name="fastestLapSpeed")

    status_id = Mapped[int] = mapped_column(name="statusId", nullable=False)

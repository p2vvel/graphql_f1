from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class Result(Base):
    __tablename__ = "results"

    id: Mapped[int] = mapped_column(name="resultId", primary_key=True, nullable=False)
    race_id: Mapped[int] = mapped_column(ForeignKey("races.raceId"), name="raceId", nullable=False)
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.driverId"), name="driverId", nullable=False)     # noqa: E501
    constructor_id: Mapped[int] = mapped_column(ForeignKey("constructors.constructorId"), name="constructorId", nullable=False)     # noqa: E501

    number: Mapped[int] = mapped_column(nullable=False)
    grid: Mapped[int] = mapped_column(nullable=False)
    position: Mapped[int | None]
    position_text: Mapped[str] = mapped_column(name="positionText", nullable=False)
    position_order: Mapped[int] = mapped_column(name="positionOrder", nullable=False)

    points: Mapped[float] = mapped_column(nullable=False)
    laps: Mapped[int] = mapped_column(nullable=False)

    time: Mapped[str | None]
    milliseconds: Mapped[int]

    fastestLap: Mapped[int] = mapped_column(name="fastestLap")
    rank: Mapped[int | None]

    fastest_lap_time: Mapped[str] = mapped_column(name="fastestLapTime")
    fastest_lap_speed: Mapped[str] = mapped_column(name="fastestLapSpeed")

    status_id: Mapped[int] = mapped_column(name="statusId", nullable=False)

    race: Mapped["Race"] = relationship()       # noqa: F821
    driver: Mapped["Driver"] = relationship()       # noqa: F821
    constructor: Mapped["Constructor"] = relationship()       # noqa: F821

    def __repr__(self):
        return f'<Result id={self.id} result="{self.position_text}">'

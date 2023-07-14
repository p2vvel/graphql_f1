from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class SprintResult(Base):
    __tablename__ = "sprintResults"

    id: Mapped[int] = mapped_column(name="sprintResultId", primary_key=True, nullable=False)
    race_id: Mapped[int] = mapped_column(ForeignKey("races.raceId"), name="raceId", nullable=False)
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.driverId"), name="driverId", nullable=False)     # noqa: E501
    constructor_id: Mapped[int] = mapped_column(ForeignKey("constructors.constructorId"), name="constructorId", nullable=False)     # noqa: E501

    number: Mapped[int] = mapped_column(nullable=False)
    grid: Mapped[int] = mapped_column(nullable=False)
    position: Mapped[int] = mapped_column(nullable=False)
    position_text: Mapped[str] = mapped_column(name="positionText", nullable=False)
    position_order: Mapped[int] = mapped_column(name="positionOrder", nullable=False)

    points: Mapped[float] = mapped_column(nullable=False)
    laps: Mapped[int] = mapped_column(nullable=False)

    time: Mapped[str]
    milliseconds: Mapped[int]

    fastest_lap: Mapped[int] = mapped_column(name="fastestLap")
    fastest_lap_time: Mapped[str] = mapped_column(name="fastestLapTime")

    status_id: Mapped[int] = mapped_column(ForeignKey("status.statusId"), name="statusId", nullable=False)   # noqa: E501

    race: Mapped["Race"] = relationship()       # noqa: F821
    driver: Mapped["Driver"] = relationship()       # noqa: F821
    constructor: Mapped["Constructor"] = relationship()       # noqa: F821
    status: Mapped["Status"] = relationship()       # noqa: F821

    def __repr__(self):
        return f'<SprintResult id={self.id}>'

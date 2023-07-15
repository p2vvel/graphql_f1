from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class DriverStanding(Base):
    __tablename__ = "driverStandings"

    id: Mapped[int] = mapped_column(name="driverStandingsId", nullable=False, primary_key=True)
    race_id: Mapped[int] = mapped_column(ForeignKey("races.raceId"), name="raceId", nullable=False)
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.driverId"), name="driverId", nullable=False)    # noqa: E501

    points: Mapped[float] = mapped_column(nullable=False)
    position: Mapped[int]
    position_text: Mapped[str] = mapped_column(name="positionText")
    wins: Mapped[int] = mapped_column(nullable=False)

    race: Mapped["Race"] = relationship()                   # noqa: F821
    driver: Mapped["Driver"] = relationship()               # noqa: F821

    def __repr__(self):
        return f'<DriverStanding id={self.id}>'

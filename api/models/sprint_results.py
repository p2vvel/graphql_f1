from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class SprintResult(Base):
    __tablename__ = "sprintResults"

    id: Mapped[int] = mapped_column(name="sprintResultId", primary_key=True, nullable=False)
    race_id: Mapped[int] = mapped_column(name="raceId", nullable=False)
    driver_id: Mapped[int] = mapped_column(name="driverId", nullable=False)
    constructor_id: Mapped[int] = mapped_column(name="constructorId", nullable=False)

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

    status_id: Mapped[int] = mapped_column(name="statusId", nullable=False)

    def __repr__(self):
        return f'<SprintResult id={self.id}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(SprintResult).limit(1000)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

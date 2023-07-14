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

    def __repr__(self):
        return f'<Laptime race={self.race_id} driver={self.driver_id} lap={self.lap}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(LapTime).limit(1000)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from datetime import time as time_type


class PitStops(Base):
    __tablename__ = "pitStops"

    race_id: Mapped[int] = mapped_column(name="raceId", primary_key=True, nullable=False)
    driver_id: Mapped[int] = mapped_column(name="driverId", primary_key=True, nullable=False)
    stop: Mapped[int] = mapped_column(nullable=False, primary_key=True)

    lap: Mapped[int] = mapped_column(nullable=False)
    time: Mapped[time_type] = mapped_column(nullable=False)

    duration: Mapped[str]
    milliseconds: Mapped[int]

    def __repr__(self):
        return f'<PitStop race={self.race_id} driver={self.driver_id} lap={self.lap}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(PitStops).limit(1000)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

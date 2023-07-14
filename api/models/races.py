from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
from datetime import date as date_type, time as time_type


class Race(Base):
    __tablename__ = "races"

    id: Mapped[int] = mapped_column(name="raceId", primary_key=True)
    year: Mapped[int] = mapped_column(nullable=False)
    round: Mapped[int] = mapped_column(nullable=False)
    circuit_id: Mapped[int] = mapped_column(name="circuitId", nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[date_type] = mapped_column(nullable=False)
    time: Mapped[time_type]
    url: Mapped[str] = mapped_column(unique=True)

    fp1_date: Mapped[date_type]
    fp1_time: Mapped[time_type]
    fp2_date: Mapped[date_type]
    fp2_time: Mapped[time_type]
    fp3_date: Mapped[date_type]
    fp3_time: Mapped[time_type]

    quali_date: Mapped[date_type]
    quali_time: Mapped[time_type]

    sprint_date: Mapped[date_type]
    sprint_time: Mapped[time_type]

    def __repr__(self):
        return f'<Race year={self.year} round={self.round}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(Race).limit(1000).offset(1000)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

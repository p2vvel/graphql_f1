from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class DriverStanding(Base):
    __tablename__ = "driverStandings"

    id: Mapped[int] = mapped_column(name="driverStandingsId", nullable=False, primary_key=True)
    race_id: Mapped[int] = mapped_column(name="raceId", nullable=False)
    driver_id: Mapped[int] = mapped_column(name="driverId", nullable=False)

    points: Mapped[float] = mapped_column(nullable=False)
    position: Mapped[int]
    position_text: Mapped[str] = mapped_column(name="positionText")
    wins: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f'<DriverStanding id={self.id}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(DriverStanding)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Qualifying(Base):
    __tablename__ = "qualifying"

    id: Mapped[int] = mapped_column(name="qualifyId", nullable=False, primary_key=True)
    race_id: Mapped[int] = mapped_column(name="raceId", nullable=False)
    driver_id: Mapped[int] = mapped_column(name="driverId", nullable=False)
    constructor_id: Mapped[int] = mapped_column(name="constructorId", nullable=False)
    number: Mapped[int] = mapped_column(nullable=False)
    position: Mapped[int]
    q1: Mapped[str]
    q2: Mapped[str]
    q3: Mapped[str]

    def __repr__(self):
        return f'<Qualifying id={self.id}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(Qualifying).limit(1000)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class ConstructorStanding(Base):
    __tablename__ = "constructorStandings"

    id: Mapped[int] = mapped_column(name="constructorStandingsId", nullable=False, primary_key=True)
    race_id: Mapped[int] = mapped_column(name="raceId", nullable=False)
    constructor_id: Mapped[int] = mapped_column(name="constructorId", nullable=False)

    points: Mapped[float] = mapped_column(nullable=False)
    position: Mapped[int]
    position_text: Mapped[str] = mapped_column(name="positionText")
    wins: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self):
        return f'<ConstructorStanding id={self.id}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(ConstructorStanding)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

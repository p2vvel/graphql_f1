from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class ConstructorResult(Base):
    __tablename__ = "constructorResults"

    id: Mapped[int] = mapped_column(name="constructorResultsId", primary_key=True, nullable=False)
    race_id: Mapped[int] = mapped_column(name="raceId", nullable=False)
    constructor_id: Mapped[int] = mapped_column(name="constructorId", nullable=False)
    
    points: Mapped[float]
    status: Mapped[str]

    def __repr__(self):
        return f'<ConstructorResult id={self.id}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(ConstructorResult)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

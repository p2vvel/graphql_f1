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

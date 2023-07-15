from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class ConstructorStanding(Base):
    __tablename__ = "constructorStandings"

    id: Mapped[int] = mapped_column(name="constructorStandingsId", nullable=False, primary_key=True)
    race_id: Mapped[int] = mapped_column(ForeignKey("races.raceId"), name="raceId", nullable=False)
    constructor_id: Mapped[int] = mapped_column(ForeignKey("constructors.constructorId"), name="constructorId", nullable=False)     # noqa: E501

    points: Mapped[float] = mapped_column(nullable=False)
    position: Mapped[int]
    position_text: Mapped[str] = mapped_column(name="positionText")
    wins: Mapped[int] = mapped_column(nullable=False)

    constructor: Mapped["Constructor"] = relationship()     # noqa: F821
    race: Mapped["Race"] = relationship()                   # noqa: F821

    def __repr__(self):
        return f'<ConstructorStanding id={self.id}>'

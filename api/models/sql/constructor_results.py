from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class ConstructorResult(Base):
    __tablename__ = "constructorResults"

    id: Mapped[int] = mapped_column(name="constructorResultsId", primary_key=True, nullable=False)
    race_id: Mapped[int] = mapped_column(ForeignKey("races.raceId"), name="raceId", nullable=False, )
    constructor_id: Mapped[int] = mapped_column(ForeignKey("constructors.constructorId"), name="constructorId", nullable=False)     # noqa: E501

    points: Mapped[float | None]
    status: Mapped[str | None]

    constructor: Mapped["Constructor"] = relationship()     # noqa: F821
    race: Mapped["Race"] = relationship()                   # noqa: F821

    def __repr__(self):
        return f'<ConstructorResult id={self.id}>'

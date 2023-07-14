from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base


class Qualifying(Base):
    __tablename__ = "qualifying"

    id: Mapped[int] = mapped_column(name="qualifyId", nullable=False, primary_key=True)
    race_id: Mapped[int] = mapped_column(ForeignKey("races.raceId"), name="raceId", nullable=False)
    driver_id: Mapped[int] = mapped_column(ForeignKey("drivers.driverId"), name="driverId", nullable=False)   # noqa: E501
    constructor_id: Mapped[int] = mapped_column(ForeignKey("constructors.constructorId"), name="constructorId", nullable=False)     # noqa: E501
    number: Mapped[int] = mapped_column(nullable=False)
    position: Mapped[int]
    q1: Mapped[str]
    q2: Mapped[str]
    q3: Mapped[str]

    race: Mapped["Race"] = relationship()       # noqa: F821
    driver: Mapped["Driver"] = relationship()       # noqa: F821
    constructor: Mapped["Constructor"] = relationship()       # noqa: F821

    def __repr__(self):
        return f'<Qualifying id={self.id}>'

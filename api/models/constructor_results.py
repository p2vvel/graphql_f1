from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class ConstructorResult(Base):
    __tablename__ = "constructorResults"

    id: Mapped[int] = mapped_column(name="constructorResultsId", primary_key=True, nullable=False)
    race_id: Mapped[int] = mapped_column(name="raceId", nullable=False)
    constructor_id: Mapped[int] = mapped_column(name="constructorId", nullable=False)
    
    points: Mapped[float]
    status: Mapped[str]

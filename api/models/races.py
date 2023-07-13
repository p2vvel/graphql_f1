from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Time, Date
from .base import Base


class Race(Base):
    __tablename__ = "races"

    id: Mapped[int] = mapped_column(name="raceId", primary_key=True)
    year: Mapped[int] = mapped_column(nullable=False)
    round: Mapped[int] = mapped_column(nullable=False)
    circuit_id: Mapped[int] = mapped_column(name="circuitId", nullable=False)    
    name: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[Date] = mapped_column(nullable=False)
    time: Mapped[Time]
    url: Mapped[str] = mapped_column(unique=True)

    fp1_date: Mapped[Date]
    fp1_time: Mapped[Time]
    fp2_date: Mapped[Date]
    fp2_time: Mapped[Time]
    fp3_date: Mapped[Date]
    fp3_time: Mapped[Time]

    quali_date: Mapped[Date]
    quali_time: Mapped[Time]

    sprint_date: Mapped[Date]
    sprint_time: Mapped[Time]

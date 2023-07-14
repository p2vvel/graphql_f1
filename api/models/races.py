from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base
from datetime import date as date_type, time as time_type


class Race(Base):
    __tablename__ = "races"

    id: Mapped[int] = mapped_column(name="raceId", primary_key=True)
    year: Mapped[int] = mapped_column(nullable=False)
    round: Mapped[int] = mapped_column(nullable=False)
    circuit_id: Mapped[int] = mapped_column(ForeignKey("circuits.circuitId"), name="circuitId", nullable=False)    # noqa: E501
    name: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[date_type] = mapped_column(nullable=False)
    time: Mapped[time_type]
    url: Mapped[str] = mapped_column(unique=True)

    fp1_date: Mapped[date_type]
    fp1_time: Mapped[time_type]
    fp2_date: Mapped[date_type]
    fp2_time: Mapped[time_type]
    fp3_date: Mapped[date_type]
    fp3_time: Mapped[time_type]

    quali_date: Mapped[date_type]
    quali_time: Mapped[time_type]

    sprint_date: Mapped[date_type]
    sprint_time: Mapped[time_type]

    circuit: Mapped["Circuit"] = relationship()       # noqa: F821

    def __repr__(self):
        return f'<Race year={self.year} round={self.round}>'

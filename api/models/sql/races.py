from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from .base import Base
from datetime import date as date_type, time as time_type
from sqlalchemy.ext.hybrid import hybrid_property


class Race(Base):
    __tablename__ = "races"

    id: Mapped[int] = mapped_column(name="raceId", primary_key=True)
    year: Mapped[int] = mapped_column(ForeignKey("seasons.year"), nullable=False)
    round: Mapped[int] = mapped_column(nullable=False)
    circuit_id: Mapped[int] = mapped_column(ForeignKey("circuits.circuitId"), name="circuitId", nullable=False)    # noqa: E501
    name: Mapped[str] = mapped_column(nullable=False)
    date: Mapped[date_type] = mapped_column(nullable=False)
    time: Mapped[time_type | None]
    url: Mapped[str] = mapped_column(unique=True)

    fp1_date: Mapped[date_type | None]
    fp1_time: Mapped[time_type | None]
    fp2_date: Mapped[date_type | None]
    fp2_time: Mapped[time_type | None]
    fp3_date: Mapped[date_type | None]
    fp3_time: Mapped[time_type | None]

    quali_date: Mapped[date_type | None]
    quali_time: Mapped[time_type | None]

    sprint_date: Mapped[date_type | None]
    sprint_time: Mapped[time_type | None]

    circuit: Mapped["Circuit"] = relationship()         # noqa: F821
    season: Mapped["Season"] = relationship()           # noqa: F821

    results: Mapped[list["Result"]] = relationship(order_by="Result.position_order.asc()")      # noqa: F821, E501
    qualies: Mapped[list["Qualifying"]] = relationship(order_by="Qualifying.position.asc()")    # noqa: F821, E501

    @hybrid_property
    def last_race(self) -> bool:
        return self.round == self.season.last_round

    driver_standings: Mapped[list["DriverStanding"]] = relationship(order_by="DriverStanding.position.asc()")      # noqa: F821, E501
    constructor_standings: Mapped[list["ConstructorStanding"]] = relationship(order_by="ConstructorStanding.position.asc()")    # noqa: F821, E501

    def __repr__(self):
        return f'<Race year={self.year} round={self.round}>'

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import select
from sqlalchemy.ext.hybrid import hybrid_property
from .base import Base
from sqlalchemy import SQLColumnExpression
from sqlalchemy.sql import functions as sql_fun
from . import Race, Result, DriverStanding


class Season(Base):
    __tablename__ = "seasons"

    year: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    url: Mapped[str] = mapped_column(nullable=False, unique=True)

    races: Mapped[list["Race"]] = relationship(order_by="Race.round.asc()")

    @hybrid_property
    def last_round(self) -> int:
        if self.races:
            return self.races[-1].round

    # TODO: last_round expression
    @last_round.inplace.expression
    @classmethod
    def _last_round_expression(cls) -> SQLColumnExpression[int]:
        stmt = (select(sql_fun.max(Race.round))
                .where(Race.year == cls.year)
                .label("last_round"))
        return stmt

    driver_standings: Mapped[list["DriverStanding"]] = relationship(secondary="races")      # noqa: F821

    @hybrid_property
    def latest_round(self) -> int:
        return max([k.round for k in self.races if k.results != []])

    @latest_round.inplace.expression
    @classmethod
    def _latest_round_expression(cls) -> SQLColumnExpression[int]:
        stmt = (select(sql_fun.max(Race.round))
                .join(Result, Result.race_id == Race.id)
                .where(Race.year == cls.year)
                .label("latest_round"))
        return stmt

    latest_driver_standings: Mapped[list["DriverStanding"]] = relationship(     # noqa: F821
        primaryjoin="and_(Season.year==Race.year, Race.round==Season.latest_round)",
        secondary="races",
        order_by="DriverStanding.position.asc()",
        viewonly=True
        )

    latest_constructor_standings: Mapped[list["ConstructorStanding"]] = relationship(   # noqa: F821
        primaryjoin="and_(Season.year==Race.year, Race.round==Season.latest_round)",
        secondary="races",
        order_by="ConstructorStanding.position.asc()",
        viewonly=True
        )

    def __repr__(self):
        return f'<Season year={self.year}>'

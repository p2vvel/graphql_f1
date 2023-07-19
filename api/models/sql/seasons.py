from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property
from .base import Base
from .races import Race
from sqlalchemy import ColumnElement



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

    def __repr__(self):
        return f'<Season year={self.year}>'

from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Season(Base):
    __tablename__ = "seasons"

    year: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    url: Mapped[str] = mapped_column(nullable=False, unique=True)

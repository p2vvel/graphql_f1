from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Constructor(Base):
    __tablename__ = "constructors"

    id: Mapped[int] = mapped_column(name="constructorId", nullable=False, primary_key=True)
    constructor_ref: Mapped[str] = mapped_column(name="constructorRef", nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    nationality: Mapped[str]
    url: Mapped[str] = mapped_column(nullable=False, unique=True)

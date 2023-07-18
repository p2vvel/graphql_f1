from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Circuit(Base):
    __tablename__ = "circuits"

    id: Mapped[int] = mapped_column(name="circuitId", nullable=False, primary_key=True)
    circuit_ref: Mapped[str] = mapped_column(name="circuitRef", nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    location: Mapped[str | None]
    country: Mapped[str | None]
    lat: Mapped[float | None]
    lng: Mapped[float | None]
    alt: Mapped[int | None]
    url: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __repr__(self):
        return f"<Circuit: \"{self.name}\">"

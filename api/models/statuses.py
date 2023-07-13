from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Status(Base):
    __tablename__ = "status"

    id: Mapped[int] = mapped_column(name="statusId", nullable=False, primary_key=True)
    status: Mapped[str] = mapped_column(nullable=False, server_default=" ")

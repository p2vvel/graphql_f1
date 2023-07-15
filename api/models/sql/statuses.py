from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Status(Base):
    __tablename__ = "status"

    id: Mapped[int] = mapped_column(name="statusId", nullable=False, primary_key=True)
    status: Mapped[str] = mapped_column(nullable=False, server_default=" ")

    def __repr__(self):
        return f'<Status desc="{self.status}">'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(Status)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

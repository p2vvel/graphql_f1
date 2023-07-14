from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class Season(Base):
    __tablename__ = "seasons"

    year: Mapped[int] = mapped_column(nullable=False, primary_key=True)
    url: Mapped[str] = mapped_column(nullable=False, unique=True)

    def __repr__(self):
        return f'<Season year={self.year}>'


if __name__ == "__main__":
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(Season)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

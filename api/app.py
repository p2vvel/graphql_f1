

if __name__ == "__main__":
    from api import models
    from sqlalchemy import select
    from api.db import get_db
    db = next(get_db())
    query = select(models.SprintResult).limit(1000)
    data = db.scalars(query)
    temp = [k for k in data]
    print(temp)

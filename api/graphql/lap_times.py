from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class LapTime(SQLAlchemyObjectType):
    class Meta:
        model = models.LapTime

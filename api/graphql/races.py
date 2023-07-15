from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class Race(SQLAlchemyObjectType):
    class Meta:
        model = models.Race

from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class Qualifying(SQLAlchemyObjectType):
    class Meta:
        model = models.Qualifying

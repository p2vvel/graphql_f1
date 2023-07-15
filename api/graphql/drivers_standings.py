from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class DriverStanding(SQLAlchemyObjectType):
    class Meta:
        model = models.DriverStanding

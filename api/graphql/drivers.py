from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class Driver(SQLAlchemyObjectType):
    class Meta:
        model = models.Driver

from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class Status(SQLAlchemyObjectType):
    class Meta:
        model = models.Status

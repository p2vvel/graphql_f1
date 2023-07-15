from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class SprintResult(SQLAlchemyObjectType):
    class Meta:
        model = models.SprintResult

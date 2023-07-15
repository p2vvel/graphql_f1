from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class ConstructorResult(SQLAlchemyObjectType):
    class Meta:
        model = models.ConstructorResult

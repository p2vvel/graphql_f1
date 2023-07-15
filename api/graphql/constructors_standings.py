from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class ConstructorStanding(SQLAlchemyObjectType):
    class Meta:
        model = models.ConstructorStanding

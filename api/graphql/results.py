from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class Result(SQLAlchemyObjectType):
    class Meta:
        model = models.Result

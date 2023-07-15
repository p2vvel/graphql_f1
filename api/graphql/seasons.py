from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class Season(SQLAlchemyObjectType):
    class Meta:
        model = models.Season

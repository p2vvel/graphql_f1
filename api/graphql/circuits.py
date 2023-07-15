from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class Circuit(SQLAlchemyObjectType):
    class Meta:
        model = models.Circuit

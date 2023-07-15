from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class Constructor(SQLAlchemyObjectType):
    class Meta:
        model = models.Constructor

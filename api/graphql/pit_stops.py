from graphene_sqlalchemy import SQLAlchemyObjectType
from api import models


class PitStops(SQLAlchemyObjectType):
    class Meta:
        model = models.PitStops

from fastapi import FastAPI
from graphene import ObjectType, Schema, String
from starlette_graphene3 import GraphQLApp


class Query(ObjectType):
    hello = String(imie=String(default_value="pszemas"))
    goodbye = String()

    def resolve_hello(root, info, imie):
        return f"Hello, {imie}!"

    def resolve_goodbye(root, info):
        return "Elo mordo"


app = FastAPI()
app.mount("/", GraphQLApp(schema=Schema(query=Query)))

from contextlib import asynccontextmanager

import strawberry
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from strawberry.fastapi import GraphQLRouter

from app.db.db import close_db, initialize_db
from app.strawberry import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    await initialize_db()
    yield
    await close_db()


schema = strawberry.Schema(query=models.Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI(lifespan=lifespan)
app.include_router(graphql_app, prefix="/graphql")


@app.get("/")
def root_to_graphql_redirect():
    return RedirectResponse("/graphql")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app)

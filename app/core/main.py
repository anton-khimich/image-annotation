import graphene
import mongoengine
import app.core.schema
from fastapi import FastAPI
from starlette.graphql import GraphQLApp


my_schema = graphene.Schema(query=app.core.schema.Query, mutation=app.core.schema.Mutations)
app = FastAPI()


@app.on_event("startup")
async def create_db_client():
    mongoengine.connect('annotation')


@app.on_event("shutdown")
async def shutdown_db_client():
    mongoengine.disconnect('annotation')


app.add_route('/', GraphQLApp(my_schema))

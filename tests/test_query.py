from graphene.test import Client
import graphene
from context import schema

my_schema = graphene.Schema(query=schema.Query, mutation=schema.Mutations)


def test_add_task():
    client = Client(my_schema)
    query = '''{hey}'''
    expected = {
        'data': {
            'hey': 'Hello'
        }
    }
    executed = client.execute(query)
    assert executed == expected

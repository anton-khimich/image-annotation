import pytest
import graphene
import mongoengine
from graphene.test import Client
from context import schema


def setup_function():
    mongoengine.connect('annotationtest', host='mongomock://localhost')


def teardown_function():
    mongoengine.disconnect()


@pytest.fixture
def get_schema():
    return graphene.Schema(query=schema.Query, mutation=schema.Mutations)


def test_get_unassigned_tasks(get_schema):
    client = Client(get_schema)
    query = '''query getUnassignedTasks {
                unassignedTasks {
                    id
                }
            }'''
    expected = {
        'data': {
            'unassignedTasks': []
        }
    }
    executed = client.execute(query)
    assert executed == expected

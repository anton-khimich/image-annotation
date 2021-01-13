from graphene import ObjectType, ID, String, List
from graphql_api.annotation.types import AnnotationOutput


class TaskOutput(ObjectType):
    id = ID()
    title = String()
    image_url = String()
    annotations = List(AnnotationOutput)
    assigned = String()

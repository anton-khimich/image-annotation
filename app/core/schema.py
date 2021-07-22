from graphene import ObjectType, Field, ID, List
from app.core.graphql_api.task.types import TaskOutput
from app.core.graphql_api.task.resolvers import resolve_task, resolve_unassigned_tasks
from app.core.graphql_api.task.mutations import (AddTask, AssignTask, CompleteTask,
                                        DeleteTask)


class Mutations(ObjectType):
    add_task = AddTask.Field()
    assign_task = AssignTask.Field()
    complete_task = CompleteTask.Field()
    delete_task = DeleteTask.Field()


class Query(ObjectType):
    task = Field(TaskOutput, id=ID(required=True), resolver=resolve_task)
    unassigned_tasks = List(TaskOutput, resolver=resolve_unassigned_tasks)

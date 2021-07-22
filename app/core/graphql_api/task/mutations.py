from graphene import Mutation, Field, String, Boolean, ID, List
from app.core.models.task import Task
from app.core.graphql_api.annotation.types import AnnotationInput


class AddTask(Mutation):
    class Arguments:
        title = String(required=True)
        image_url = String(required=True)

    ok = Boolean()
    id = Field(ID)

    def mutate(parent, info, title, image_url):
        task = Task(title=title, image_url=image_url)
        task.save()
        ok = True
        return AddTask(id=task.id, ok=ok)


class AssignTask(Mutation):
    class Arguments:
        id = ID(required=True)
        assigned = String(required=True)

    ok = Boolean()

    def mutate(parent, info, id, assigned):
        task = Task.objects(id=id).get()
        if task.assigned is None:
            ok = True
            task.assigned = assigned
            task.save()
        else:
            ok = False

        return AssignTask(ok=ok)


class CompleteTask(Mutation):
    class Arguments:
        id = ID(required=True)
        annotations = List(AnnotationInput)

    ok = Boolean()

    def mutate(parent, info, id, annotations):
        task = Task.objects(id=id).get()
        task.update(push__annotations__0=annotations)
        ok = True
        return CompleteTask(ok=ok)


class DeleteTask(Mutation):
    class Arguments:
        id = ID(required=True)

    ok = Boolean()

    def mutate(parent, info, id):
        task = Task(id=id)
        task.delete()
        ok = True
        return DeleteTask(ok=ok)

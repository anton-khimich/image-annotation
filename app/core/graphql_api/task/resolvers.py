from app.core.models.task import Task


def resolve_task(parent, info, id):
    return Task.objects(id=id).get()


def resolve_unassigned_tasks(parent, info):
    unassigned_tasks = Task.objects(assigned=None).limit(10)
    return unassigned_tasks

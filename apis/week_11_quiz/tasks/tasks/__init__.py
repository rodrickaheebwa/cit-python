from tasks.tasks.resource import TasksResource

def tasks_routes(api):
    api.add_resource(TasksResource, '/tasks', '/tasks/<int:task_id>')
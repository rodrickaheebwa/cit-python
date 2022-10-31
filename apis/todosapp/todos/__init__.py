from todosapp.todos.resource import Todos

def todos_routes(api):
    api.add_resource(Todos, '/api/todos', '/api/todos/<int:todo_id>')
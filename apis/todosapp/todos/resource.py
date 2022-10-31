from datetime import datetime
from todosapp.models import Todo
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource, reqparse
from todosapp.schemas.app_schemas import TodoSchema

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

class Todos(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    # http method : get
    @jwt_required()
    def get(self, todo_id = None):
        if todo_id:
            todo = Todo.get_todo_by_id(todo_id)
            if todo:
                return todo_schema.dump(todo), 200
            return {'message': 'Todo not found'}, 404

        user_id = get_jwt_identity()
        user_todos = Todo.get_user_todos(user_id)
        return todos_schema.dump(user_todos), 200

    # http method : post
    @jwt_required()
    def post(self):
        self.parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
        self.parser.add_argument('description', type=str, required=True, help='Description cannot be blank')
        self.parser.add_argument('due_date', type=str, required=True, help='Due date cannot be blank')

        data = self.parser.parse_args()
        data['due_date'] = datetime.strptime(data['due_date'], '%Y-%m-%d')

        user_id = get_jwt_identity()

        todo = Todo.query.filter_by(title=data['title']).first()
        if todo:
            return {'message' : f"{data['title']} is already in the list"}, 400
        else:
            new_todo = Todo(**data, created_by=user_id)
            new_todo.save()
            return {'message' : f"added {data['title']} to todo list"}, 201

    # http method : delete
    @jwt_required()
    def delete(self, todo_id):
        user_id = get_jwt_identity()
        todo = Todo.get_todo_by_id(todo_id)

        if not todo:
            return {'message' : 'Todo not found'}, 404

        if todo.created_by != user_id:
            return {'message': 'You are not authorized to delete this todo'}, 401

        todo.delete()
        return {'message' : f"todo {todo.title} deleted successfully"}, 200
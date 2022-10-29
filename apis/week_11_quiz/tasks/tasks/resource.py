from datetime import datetime
from tasks.models import Task
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from tasks.schemas.app_schemas import TaskSchema

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

class TasksResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, task_id = None):
        if task_id:
            task = Task.get_task_by_id(task_id)
            if task:
                return task_schema.dump(task), 200
            else:
                return {'message' : 'task not found'}, 404

        user_id = get_jwt_identity()
        tasks  = Task.get_user_tasks(user_id)
        return tasks_schema.dump(tasks)

    @jwt_required()
    def post(self):
        self.parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
        self.parser.add_argument('description', type=str, required=True, help='Description cannot be blank')
        self.parser.add_argument('due_date', type=str, required=True, help='Due date cannot be blank')
        self.parser.add_argument('complete', type=bool)

        data = self.parser.parse_args()
        data['due_date'] = datetime.strptime(data['due_date'], '%Y-%m-%d')

        user_id = get_jwt_identity()
        new_task = Task(**data, created_by=user_id)
        new_task.save()
        return {'message': f'Task {new_task.title} created successfully'}, 201

    @jwt_required()
    def put(self, task_id = None):
        self.parser.add_argument('title', type=str)
        self.parser.add_argument('description', type=str)
        self.parser.add_argument('due_date', type=str)
        self.parser.add_argument('complete', type=bool)
        self.parser.add_argument('created_by', type=int)

        data = self.parser.parse_args()

        if task_id:
            task = Task.query.filter_by(id=task_id).first()
            if task:

                user_id = get_jwt_identity()
                if user_id != task.created_by:
                    return {'message' : 'You are not authorised to update this task'}, 401
                
                task.title = data['title'] if data['title'] else task.title
                task.description = data['description'] if data['description'] else task.description
                task.complete = data['complete'] if data['complete'] else task.complete
                task.created_by = data['created_by'] if data['created_by'] else task.created_by
                task.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d') if data['due_date'] else task.due_date
                task.update()
                return {'message' : 'Task updated successfully'}, 201
            else:
                return {'message' : 'Task not found'}, 404
        return {'message' : 'Pass in an id for the task'}, 400

    @jwt_required()
    def delete(self, task_id = None):
        if task_id:
            task = Task.query.filter_by(id=task_id).first()
            if task:

                user_id = get_jwt_identity()
                if user_id != task.created_by:
                    return {'message' : 'You are not authorised to delete this task'}, 401

                task.delete()
                return {'message' : f'Task {task.title} deleted successfully'}, 200
            else:
                return {'message' : 'Task not found'}, 404
        return {'message' : 'Pass in an id for a task'}, 400
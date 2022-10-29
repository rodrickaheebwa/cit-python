from tasks.models import User
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from tasks.schemas.app_schemas import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Users(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    @jwt_required()
    def get(self, user_id = None):
        if user_id:
            current_id = get_jwt_identity()
            if user_id == current_id:
                user = User.query.filter_by(id=user_id).first()
                if user:
                    return user_schema.dump(user), 200
                else:
                    return {'message' : 'User not found'}, 400
            else:
                return {'message' : 'you cannot access information from another account'}, 401
        users = User.get_all_users()
        return users_schema.dump(users), 200

    @jwt_required()
    def put(self, user_id):
        self.parser.add_argument('name', type=str)
        self.parser.add_argument('email', type=str)
        self.parser.add_argument('password', type=str)

        data = self.parser.parse_args()

        current_id = get_jwt_identity()

        if user_id == current_id:
            user = User.query.filter_by(id=user_id).first()
            if user:
                user.name = data['name'] if data['name'] else user.name
                user.email = data['email'] if data['email'] else user.email
                user.password = User.hash_password(data['password']) if data['password'] else user.password
                user.update()
                return {'message' : 'User updated successfully'}, 201
            else:
                return {'message' : 'User not found'}, 404
        else:
            return {'message' : 'you are not authorised to update this user'}, 401
        # return {'message' : 'Pass in an id'}, 400

    @jwt_required()
    def delete(self, user_id = None):
        if user_id:
            current_id = get_jwt_identity()
            if user_id == current_id:
                user = User.query.filter_by(id=user_id).first()
                if user:
                    user.delete()
                    # how to delete token/ end session
                    return {'message' : 'User deleted successfully'}, 200
                else:
                    return {'message' : 'User not found'}, 404
            return {'message' : 'You are not authorised to delete this account'}, 401
        return {'message' : 'An id is required'}, 400
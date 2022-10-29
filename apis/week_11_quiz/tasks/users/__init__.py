from tasks.users.resource import Users

def users_routes(api):
    api.add_resource(Users, '/users', '/users/<int:user_id>')
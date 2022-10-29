from tasks.auth.resource import Login, Register

def auth_routes(api):
    api.add_resource(Login, '/auth/login')
    api.add_resource(Register, '/auth/register')
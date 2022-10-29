from sqlalchemy import MetaData
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
ma = Marshmallow()
migrate = Migrate()
api = Api()
jwt = JWTManager()
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tasks.db"
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    from .errors.handlers import errors as error_views
    app.register_blueprint(error_views)

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user['id']

    @jwt.user_lookup_loader
    def user_lookup_callback(_jwt_header, jwt_data):
        from tasks.models import User
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()

    return app

from .auth import auth_routes
from .users import users_routes
from .tasks import tasks_routes

auth_routes(api)
users_routes(api)
tasks_routes(api)
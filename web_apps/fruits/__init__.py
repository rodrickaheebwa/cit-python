import os
from flask import Flask
from .config import app_config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

# db variable initialization
db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

def create_app():
    # create flask instance
    app = Flask(__name__, template_folder=TEMPLATE_FOLDER)
    app.config.from_object(app_config['development'])
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from .views.fruits_view import views as fruits_view
    from .views.hacker_news_view import hviews as hacker_news_views
    from .views.user_view import userviews as user_views
    from .views.cbs_news_view import cbsviews as cbs_views
    
    app.register_blueprint(fruits_view)
    app.register_blueprint(hacker_news_views)
    app.register_blueprint(user_views)
    app.register_blueprint(cbs_views)

    return app
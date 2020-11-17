from typing import Type

from flask import Flask
from flask_login import LoginManager

from app.extensions import db
from app.models import get_user_by_id
from app.views import auth, main
from config import Config


def create_app(config: Type[Config]) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    configure_db(app)
    configure_login(app)
    configure_blueprint(app)
    return app


def configure_db(app: Flask):
    db.init_app(app)


def configure_login(app: Flask):
    login_manager = LoginManager(app)
    login_manager.user_loader(get_user_by_id)
    login_manager.login_view = 'auth.login'


def configure_blueprint(app: Flask):
    app.register_blueprint(auth)
    app.register_blueprint(main)

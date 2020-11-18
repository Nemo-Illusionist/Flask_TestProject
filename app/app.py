from flask import Flask

from .extensions import db, login_manager, admin
from .models import get_user_by_id, Task
from .views import auth, main, UserAdminModelView, AdminModelView
from config import Config


def create_app(config: Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    configure_db(app)
    configure_login(app)
    configure_blueprint(app)
    configure_admin(app)
    return app


def configure_db(app: Flask):
    db.init_app(app)


def configure_admin(app: Flask):
    admin.init_app(app)
    admin.add_view(UserAdminModelView(db.session))
    admin.add_view(AdminModelView(Task, db.session))


def configure_login(app: Flask):
    login_manager.init_app(app)
    login_manager.user_loader(get_user_by_id)
    login_manager.login_view = 'auth.login'


def configure_blueprint(app: Flask):
    app.register_blueprint(auth)
    app.register_blueprint(main)

from flask import Flask

from app.extensions import db, login_manager, admin
from app.models import get_user_by_id
from app.views import main
from app.views.admin import UserAdminModelView, AuthAdminIndexView, TaskAdminModelView
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
    admin.init_app(app, AuthAdminIndexView())
    admin.name = 'Flask test project'
    admin.base_template = 'admin/master.html'
    admin.template_mode = 'bootstrap3'
    admin.add_view(UserAdminModelView(db.session))
    admin.add_view(TaskAdminModelView(db.session))


def configure_login(app: Flask):
    login_manager.init_app(app)
    login_manager.user_loader(get_user_by_id)
    login_manager.login_view = 'auth.login'


def configure_blueprint(app: Flask):
    app.register_blueprint(main)

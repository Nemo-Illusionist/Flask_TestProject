from flask_admin.contrib.sqlamodel import ModelView
from flask_login import current_user

from app.models import User


class AdminModelView(ModelView):
    action_disallowed_list = ['delete']

    def is_accessible(self):
        return current_user.is_authenticated


class UserAdminModelView(AdminModelView):
    excluded_list_columns = ('password_hash',)

    def __init__(self, session, **kwargs):
        super(UserAdminModelView, self).__init__(User, session, **kwargs)

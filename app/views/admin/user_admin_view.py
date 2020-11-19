from .admin_view import AdminModelView
from app.models import User


class UserAdminModelView(AdminModelView):
    column_exclude_list = ['password_hash', ]

    def __init__(self, session, **kwargs):
        super(UserAdminModelView, self).__init__(User, session, **kwargs)

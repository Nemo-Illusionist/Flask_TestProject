from .admin_view import AdminModelView
from app.models import User


class UserAdminModelView(AdminModelView):
    column_exclude_list = ['password_hash', ]
    form_excluded_columns = ['tasks', ]

    def __init__(self, session, **kwargs):
        super().__init__(User, session, **kwargs)

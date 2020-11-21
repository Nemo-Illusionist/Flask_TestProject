from app.models import User
from .admin_view import AdminModelView


class UserAdminModelView(AdminModelView):
    column_exclude_list = ['password_hash', ]
    form_excluded_columns = ['tasks', ]

    def __init__(self, session, name=None, category=None, endpoint=None, url=None, static_folder=None,
                 menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        super().__init__(User, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type,
                         menu_icon_value)

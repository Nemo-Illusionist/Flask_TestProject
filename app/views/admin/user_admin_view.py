from sqlalchemy import func

from app.models import User, Task
from .admin_view import AdminModelView, AdminReadOnlyModelView


class UserAdminModelView(AdminModelView):
    column_exclude_list = ['password_hash', ]
    form_excluded_columns = ['tasks', ]

    def __init__(self, session, name=None, category=None, endpoint=None, url=None, static_folder=None,
                 menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        super().__init__(User, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type,
                         menu_icon_value)


class UserStatisticAdminModelView(AdminReadOnlyModelView):
    column_list = ['username', 'task_count']

    def get_query(self):
        return self.session.query(
            User.id,
            User.username,
            func.count(Task.id).label('task_count')
        ).select_from(User).join(Task).group_by(User.id, User.username)

    def __init__(self, session, name=None, category=None, endpoint=None, url=None, static_folder=None,
                 menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        super().__init__(User, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type,
                         menu_icon_value)

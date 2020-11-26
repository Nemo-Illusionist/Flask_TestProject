from flask_login import current_user
from sqlalchemy import func

from app.models import User, Task
from .admin_view import AdminModelView, AdminReadOnlyModelView


class UserAdminModelView(AdminModelView):
    column_exclude_list = ['password_hash', ]
    form_excluded_columns = ['tasks', ]

    def on_model_change(self, form, model: User, is_created):
        if is_created or form.password_hash.object_data != model.password_hash:
            model.set_password(model.password_hash)

    def __init__(self, session, name=None, category=None, endpoint=None, url=None, static_folder=None,
                 menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        super().__init__(User, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type,
                         menu_icon_value)


class UserStatisticAdminModelView(AdminReadOnlyModelView):
    column_list = ['username', 'task_count']

    def is_accessible(self):
        return current_user.is_authenticated and (current_user.is_superuser or current_user.can_review_tasks)

    def get_query(self):
        return self.session.query(
            User.id,
            User.username,
            func.count(Task.id).label('task_count')
        ).select_from(User).outerjoin(Task).group_by(User.id, User.username)

    def __init__(self, session, name=None, category=None, endpoint=None, url=None, static_folder=None,
                 menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        super().__init__(User, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type,
                         menu_icon_value)

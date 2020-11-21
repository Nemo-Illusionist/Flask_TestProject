from flask_login import current_user

from .admin_view import AdminModelView
from ...models import Task, get_user_by_id


class TaskAdminModelView(AdminModelView):

    def create_form(self, obj=None):
        form = super().create_form(obj)
        if not form.user.data:
            form.user.data = get_user_by_id(current_user.id)
            form.user.raw_data = [current_user.id]
        return form

    def create_model(self, form):
        return super().create_model(form)

    def __init__(self, session, name=None, category=None, endpoint=None, url=None, static_folder=None,
                 menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        super().__init__(Task, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type,
                         menu_icon_value)
        self.form_widget_args['user'] = {'disabled': True}

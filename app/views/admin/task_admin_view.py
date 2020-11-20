from flask_login import current_user

from .admin_view import AdminModelView
from ...models import Task, get_user_by_id


class TaskAdminModelView(AdminModelView):

    def create_form(self, obj=None):
        form = super().create_form(obj)
        if not form.user.data:
            form.user.data = get_user_by_id(current_user.id)
        return form

    def __init__(self, session, **kwargs):
        super().__init__(Task, session, **kwargs)
        self.form_widget_args['user'] = {'disabled': True}

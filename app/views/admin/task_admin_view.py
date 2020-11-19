from .admin_view import AdminModelView
from app.models import Task


class TaskAdminModelView(AdminModelView):

    def __init__(self, session, **kwargs):
        super(TaskAdminModelView, self).__init__(Task, session, **kwargs)

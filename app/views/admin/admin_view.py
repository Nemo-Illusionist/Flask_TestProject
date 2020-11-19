from flask import url_for, request, redirect
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class AdminModelView(ModelView):

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False

        self.can_edit = current_user.is_superuser
        self.can_delete = current_user.is_superuser
        self.can_create = current_user.is_superuser
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.login_view', next=request.url))

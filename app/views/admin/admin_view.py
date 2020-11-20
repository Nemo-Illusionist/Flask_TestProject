from datetime import datetime

from flask import url_for, request, redirect
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class AdminModelView(ModelView):
    form_widget_args = {
        'created_at': {
            'disabled': True
        },
        'updated_at': {
            'disabled': True
        },
    }

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False

        self.can_edit = current_user.is_superuser
        self.can_delete = current_user.is_superuser
        self.can_create = current_user.is_superuser
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.login_view', next=request.url))

    def create_form(self, obj=None):
        form = super().create_form(obj)
        form.created_at.data = form.updated_at.data = datetime.utcnow()
        return form

from datetime import datetime

from flask import url_for, request, redirect
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


def _date_format(view, value):
    return value.strftime('%Y-%m-%d %H:%M:%S')


class AdminModelView(ModelView):
    form_widget_args = {
        'created_at': {
            'disabled': True
        },
        'updated_at': {
            'disabled': True
        },
    }

    def __init__(self, model, session, name=None, category=None, endpoint=None, url=None, static_folder=None,
                 menu_class_name=None, menu_icon_type=None, menu_icon_value=None):
        super().__init__(model, session, name, category, endpoint, url, static_folder, menu_class_name, menu_icon_type,
                         menu_icon_value)
        self.column_type_formatters[datetime] = _date_format

    def is_accessible(self):
        if not current_user.is_authenticated:
            return False

        self.create_form(current_user.is_superuser)
        return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.login_view', next=request.url))

    def create_form(self, obj=None):
        form = super().create_form(obj)
        form.created_at.data = form.updated_at.data = datetime.utcnow()
        return form

    def set_permissions(self, is_can: bool):
        self.can_edit = self.can_delete = self.can_create = is_can


class AdminReadOnlyModelView(AdminModelView):
    can_view_details = True
    can_edit = False
    can_delete = False
    can_create = False

    def set_permissions(self, is_can: bool):
        pass

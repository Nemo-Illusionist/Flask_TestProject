from flask import url_for, request, redirect
from flask_admin import helpers, expose, AdminIndexView
from flask_login import current_user, logout_user, login_user

from ...extensions import db
from ...forms import RegistrationForm, LoginForm
from ...models import User


class AuthAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated:
            return redirect(url_for('admin.login_view'))
        return super(AuthAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = db.session.query(User).filter(User.username == form.username.data).first()
            login_user(user, remember=form.remember_me.data)

        if current_user.is_authenticated:
            return redirect(url_for('admin.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for(
            'admin.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(AuthAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()
            form.populate_obj(user)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()

            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('admin.index'))
        link = '<p>Already have an account? <a href="' + url_for(
            'admin.logout_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(AuthAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('admin.index'))

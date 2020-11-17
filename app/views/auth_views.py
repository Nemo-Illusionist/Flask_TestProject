from flask import render_template, redirect, url_for, flash, request, Response, Blueprint
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app.extensions import db
from app.forms import LoginForm, RegistrationForm
from app.models import User

auth = Blueprint('auth', __name__, url_prefix='/')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data, User.is_active).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return next_page_response()
    return render_template('auth/login.html', title='Sign In', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=form.remember_me.data)
        return next_page_response()
    return render_template('auth/register.html', title='Register', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


def next_page_response() -> Response:
    next_page = request.args.get('next')
    if not next_page or url_parse(next_page).netloc != '':
        next_page = url_for('main.index')
    return redirect(next_page)

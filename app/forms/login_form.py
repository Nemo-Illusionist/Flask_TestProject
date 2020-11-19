from flask_wtf import FlaskForm, validators
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

from app.extensions import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

    def validate_username(self, username):
        user = db.session.query(User).filter(User.username == username.data).first()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if not user.check_password(self.password.data):
            raise validators.ValidationError('Invalid password')

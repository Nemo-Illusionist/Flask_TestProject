from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import ValidationError, DataRequired, EqualTo

from app.extensions import db
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    remember_me = BooleanField('Remember Me')

    def validate_username(self, username):
        user = db.session.query(User).filter(User.username == username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

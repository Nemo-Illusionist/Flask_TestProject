from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.extensions import db
from app.models.model_mixin import TimestampMixin


class User(db.Model, UserMixin, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    is_superuser = db.Column(db.Boolean, nullable=False, default=False)
    can_review_tasks = db.Column(db.Boolean, nullable=False, default=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

    def set_password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)


def get_user_by_id(id: int) -> User:
    return User.query.filter(User.id == id, User.is_active).first()

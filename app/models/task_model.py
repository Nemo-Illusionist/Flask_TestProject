from app.extensions import db
from app.models.model_mixin import TimestampMixin


class Task(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    lower_limit = db.Column(db.Float, nullable=False)
    upper_limit = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='tasks', foreign_keys=[user_id])

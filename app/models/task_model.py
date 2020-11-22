from app.extensions import db
from app.models.model_mixin import TimestampMixin, CreatedMixin


class Task(db.Model, TimestampMixin):
    id = db.Column(db.Integer, primary_key=True)
    lower_limit = db.Column(db.Float, nullable=False)
    upper_limit = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', back_populates='tasks', foreign_keys=[user_id])

    results = db.relationship('TaskResults', back_populates='task', lazy=True)


class TaskResults(db.Model, CreatedMixin):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    task = db.relationship(Task, back_populates='results', foreign_keys=[task_id])
    task_params = db.Column(db.JSON, nullable=False)
    result = db.Column(db.Float, nullable=False)

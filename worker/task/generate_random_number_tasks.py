from app import db
from app.models import Task
from . import generate_random_number_task


def generate_random_number_tasks():
    task_ids = db.session.query(Task.id).all()
    for task_id in task_ids:
        generate_random_number_task.apply_async(task_id)

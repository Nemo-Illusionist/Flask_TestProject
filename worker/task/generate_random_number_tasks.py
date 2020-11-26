from celery import group

from app import db
from app.models import Task
from . import generate_random_number_task
from ..worker import celery


@celery.task(name='task.generate_random_number_tasks')
def generate_random_number_tasks():
    task_ids = db.session.query(Task.id).all()
    g = group(generate_random_number_task.s(task.id) for task in task_ids)
    g.apply_async()

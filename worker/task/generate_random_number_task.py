from random import randint

from app import db
from app.models import Task, TaskResults
from ..worker import celery


@celery.task(name='task.generate_random_number_task')
def generate_random_number_task(task_id: int):
    task = db.session.query(Task).filter(Task.id == task_id).first()
    task_result = TaskResults(task_id=task.id, result=randint(task.lower_limit, task.upper_limit))
    task_result.task_params = {
        'lower_limit': task.lower_limit,
        'upper_limit': task.upper_limit,
        'author_id': task.user_id
    }
    db.session.add(task_result)
    db.session.commit()

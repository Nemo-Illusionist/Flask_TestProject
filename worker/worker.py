from celery import Celery
from flask import Flask

from config import Config


def init_celery(app: Flask, config: Config) -> Celery:
    celery = Celery('tasks')
    add_context(celery, app)
    add_conf(celery, config)
    add_tasks()

    return celery


def add_conf(celery: Celery, config: Config):
    celery.conf.update(
        result_backend=config.RESULT_BACKEND,
        broker_url=config.BROKER_URL,
        timezone='UTC',
        task_serializer='json',
        accept_content=['json'],
        result_serializer='json',
        beat_schedule={
            'time_scheduler': {
                'task': 'task.generate_random_number_tasks',
                'schedule': int(config.GENERATE_RANDOM_NUMBER_TASKS_SCHEDULE)
            }
        },
    )


def add_tasks():
    # todo: import need for register tasks
    # noinspection PyUnresolvedReferences
    from . import task


def add_context(celery: Celery, app: Flask):
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

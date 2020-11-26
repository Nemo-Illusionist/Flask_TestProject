from celery import Celery
from flask import Flask

from config import Config
from .task import generate_random_number_task, generate_random_number_tasks


def create_celery(app: Flask, config: Config) -> Celery:
    celery = Celery(app.import_name)
    add_context(celery, app)
    add_conf(celery, config)
    add_tasks(celery)

    return celery


def add_conf(celery: Celery, config: Config):
    celery.conf.update(
        result_backend=config.RESULT_BACKEND,
        broker_url=config.BROKER_URL,
        timezone="UTC",
        task_serializer="json",
        accept_content=["json"],
        result_serializer="json",
        beat_schedule=config.BEAT_SCHEDULE,
    )


def add_tasks(celery: Celery):
    celery.task(generate_random_number_task)
    celery.task(generate_random_number_tasks)


def add_context(celery: Celery, app: Flask):
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

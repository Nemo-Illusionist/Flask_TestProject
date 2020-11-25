from celery import Celery

from config import Config
from .task import generate_random_number_task, generate_random_number_tasks


def create_celery(name: str, config: Config) -> Celery:
    celery = Celery(name)
    celery.conf.update(
        result_backend=config.CELERY_RESULT_BACKEND,
        broker_url=config.CELERY_BROKER_URL,
        timezone="UTC",
        task_serializer="json",
        accept_content=["json"],
        result_serializer="json",
        beat_schedule=config.CELERY_BEAT_SCHEDULE,
    )
    celery.task(generate_random_number_task)
    celery.task(generate_random_number_tasks)
    return celery

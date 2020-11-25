from celery import Celery

from .task import generate_random_number_task, generate_random_number_tasks


def create_celery(name: str, config: dict) -> Celery:
    celery = Celery(name, backend='amqp', broker=config['CELERY_BROKER_URL'])
    celery.conf.update(config)
    celery.task(generate_random_number_task)
    celery.task(generate_random_number_tasks)
    return celery

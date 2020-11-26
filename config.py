import json
import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def env_var(key, default=None, required=False, is_json=False):
    """ Parse environment variable accordingly. """
    if required:
        val = os.environ[key]
    else:
        val = os.environ.get(key, default)

    if val == 'True':
        val = True
    elif val == 'False':
        val = False

    if is_json:
        val = json.loads(val)

    return val


def get_connect_uri(driver, user, pas, host, db) -> str:
    return '{}://{}:{}@{}/{}'.format(
        driver,
        env_var(user, required=True),
        env_var(pas, required=True),
        env_var(host, required=True),
        env_var(db, required=True)
    )
    pass


class Config:
    SECRET_KEY = env_var('SECRET_KEY', required=True)

    # SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = get_connect_uri(
        'postgresql',
        'POSTGRES_USER',
        'POSTGRES_PASSWORD',
        'POSTGRES_HOST',
        'POSTGRES_DB'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = env_var('SQLALCHEMY_TRACK_MODIFICATIONS', default=False)

    # CELERY
    BROKER_URL = get_connect_uri(
        'amqp',
        'RABBITMQ_USERNAME',
        'RABBITMQ_PASSWORD',
        'RABBITMQ_HOST',
        'RABBITMQ_VHOST'
    )
    RESULT_BACKEND = get_connect_uri(
        'amqp',
        'RABBITMQ_USERNAME',
        'RABBITMQ_PASSWORD',
        'RABBITMQ_HOST',
        'RABBITMQ_VHOST'
    )
    BEAT_SCHEDULE = env_var('BEAT_SCHEDULE', default=False, is_json=True)

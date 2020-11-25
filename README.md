1. python -m venv venv
1. venv/bin/pip install -r requirements/common.txt
1. add `.env` file
1. export FLASK_APP = flask_test_project
1. flask db upgrade
1. flask run

Example .env file
```
SECRET_KEY=9da3d8c6-8d7b-4869-8867-b77eef0a6058

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=FlaskTest
POSTGRES_HOST=localhost:5432

RABBITMQ_USERNAME=rabbitmq
RABBITMQ_PASSWORD=rabbitmq
RABBITMQ_VHOST=rabbitmq
RABBITMQ_HOST=localhost:5672
BEAT_SCHEDULE="{'time_scheduler': {'task': 'generate_random_number_tasks','schedule': 300.0,}}"
```

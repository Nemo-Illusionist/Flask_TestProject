# Start project:

## docker-compose
1. add `./dockr/.env` file 
1. use command `docker-compose up -d`

### Example `./dockr/.env` file
```
SECRET_KEY=9da3d8c6-8d7b-4869-8867-b77eef0a6058

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=flask_test
POSTGRES_HOST=db:5432

RABBITMQ_USERNAME=rabbitmq
RABBITMQ_PASSWORD=rabbitmq
RABBITMQ_VHOST=rabbitmq
RABBITMQ_HOST=mq:5672
CELERY_BEAT_SCHEDULE="{\"time_scheduler\": {\"task\": \"celery.generate_random_number_tasks\",\"schedule\": 300.0}}"
```

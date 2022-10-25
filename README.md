# Start project:

## docker-compose
1. add `./dockr/.env` file 
1. use command `docker-compose up -d`
    1. `docker-compose up -d db`
    1. `docker-compose up -d mq`
    1. `docker-compose up -d web`
    1. `docker-compose up -d beat`
    1. `docker-compose up -d worker`
    1. `docker-compose up -d flower`
    

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

GENERATE_RANDOM_NUMBER_TASKS_SCHEDULE=300
```
## Task

Instruction: firstly fulfill the ​baseline​ task and send the result for review. If you feel that you can do any of ​level up​ section, let us know about that and start doing it. Before starting each new section, send the result of the previous one and let us know that you want to do the next part of the task.

Use git and private github repository (it is free) to store your source code.

If you have any troubles or questions do not hesitate to ask. Good luck!

### Baseline.

Write a flask application.

Use Flask-Login ​https://flask-login.readthedocs.io/en/latest/​ for user’s log in/sign in, Flask-Admin ​https://flask-admin.readthedocs.io/en/latest/​ for class based views,

SQLAlchemy ​https://www.sqlalchemy.org/​ as an ORM

Alembic ​https://alembic.sqlalchemy.org/en/latest/​ for migrations

Use any relational database which is supported by SQLAlchemy (for some of level ups you will need something that can be run within docker container, so if you select sqlite -- those level ups will not be available to you).

Add login/logout/registration functional. For user profile use model

User:
- username: string
- password_hash: string
- is_active: boolean
- is_superuser: boolean
- id: autoincrement integer

Also add model

Task:
- Id: autoincrement integer
- lower_limit: float
- upper_limit: float
- created_at: float
- updated_at: timestamp (utc time) (with auto updating when task is changed)
- created_by: timestamp (default utc now) (should not be updated when task is changed)

Add new view with endpoints for viewing list of tasks, viewing task details, for task update/create/delete -- all endpoints of this view should be accessible only by superuser

Add migration:
- Add field can_review_tasks to User model.

Add view with a list of usernames and amount of their tasks (accessible by superusers and users with flag can_review_tasks).

P.S. Remember that you will work in a team with other people and they will read your code. So respect their time and write code so that anyone can understand what is going on there.

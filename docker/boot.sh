#!/bin/bash
flask db upgrade
#celery -A flask_test_project.celery worker --pool=solo --loglevel=INFO
gunicorn -b :5000 --access-logfile - --error-logfile - flask_test_project:app

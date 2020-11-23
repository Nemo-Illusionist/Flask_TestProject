flask db upgrade
celery --app=flask_test_project:celery worker --pool=solo --loglevel=INFO
gunicorn -b :5000 --access-logfile - --error-logfile - flask_test_project:app

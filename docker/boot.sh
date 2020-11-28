#!/bin/bash
flask db upgrade
gunicorn -b :5000 --access-logfile - --error-logfile - flask_test_project:app

FROM python:3.8

ENV FLASK_APP flask_test_project.py

RUN adduser -D flask_test_project
USER flask_test_project

WORKDIR /home/flask_test_project

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements/docker.txt

COPY app app
COPY migrations migrations
COPY flask_test_project.py config.py boot.sh ./

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

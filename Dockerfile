FROM python:3.8-slim

ENV FLASK_APP flask_test_project.py

RUN apt update
RUN apt install -y libpq-dev python3-dev gcc

WORKDIR /app

COPY requirements /tmp/requirements
RUN pip install -r /tmp/requirements/docker.txt

COPY . .

RUN chmod +x ./docker/boot.sh

CMD ["bash", "./docker/boot.sh"]

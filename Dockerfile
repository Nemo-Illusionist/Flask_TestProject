FROM python:3.8-slim

ENV FLASK_APP flask_test_project.py

RUN apt update
RUN apt install -y libpq-dev python3-dev gcc

COPY requirements/common.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . app
WORKDIR app
#RUN chmod +x ./docker/boot.sh

#CMD ["bash", "./docker/boot.sh"]


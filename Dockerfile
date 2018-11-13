FROM python:3.7
RUN apt-get update
RUN apt-get -y upgrade
RUN pip install --upgrade pip
RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
ENV FLASK_APP server.py

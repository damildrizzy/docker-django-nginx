#pull base image
FROM python:3.8.3-alpine

#set work directory
WORKDIR /usr/src/app

#env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#psycopg dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copy project
COPY . .

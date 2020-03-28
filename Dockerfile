FROM python:3.8.2-alpine
MAINTAINER Konjing

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D konjingtuajing
USER konjingtuajing

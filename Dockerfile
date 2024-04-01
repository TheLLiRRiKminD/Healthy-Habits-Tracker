FROM python:3 as builder

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

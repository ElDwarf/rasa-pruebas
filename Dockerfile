FROM python:3.8

RUN pip install rasa[full]

WORKDIR /app

COPY src /app



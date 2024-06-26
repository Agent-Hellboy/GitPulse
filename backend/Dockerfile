# backend/Dockerfile

FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

WORKDIR /code/gitpulse

ENTRYPOINT ["/code/entrypoint.sh"]

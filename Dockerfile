FROM python:3.9-slim

RUN apt-get update && \
  apt-get install -y iputils-ping && \
  rm -rf /var/lib/apt/lists/*
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

COPY ./src /code/src
COPY ./src/config /code/config

ARG ENV
ARG CONFIG_FILE
ARG MYSQL_HOST
ARG DB_ACTIVE
ARG MYSQL_USER
ARG MYSQL_PASS
ARG MYSQL_DB
ARG MYSQL_PORT


ENV ENV=$ENV
ENV MYSQL_HOST=$MYSQL_HOST
ENV DB_ACTIVE=$DB_ACTIVE
ENV MYSQL_USER=$MYSQL_USER
ENV MYSQL_PASS=$MYSQL_PASS
ENV MYSQL_DB=$MYSQL_DB
ENV MYSQL_PORT=$MYSQL_PORT


ENV PYTHONPATH=/code/src


RUN pip install -r /code/requirements.txt
RUN pip install uvicorn
RUN mkdir -p /src/shared/infrastructure/persistence/migration/versions

COPY create_alembic.sh ./create_alembic.sh
COPY entrypoint.sh ./entrypoint.sh

RUN chmod +x ./create_alembic.sh ./entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh"]


# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["fastapi", "run", "app/main.py", "--port", "80", "--proxy-headers"]
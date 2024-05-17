#!/bin/sh

alembic -c /code/src/shared/infrastructure/persistence/alembic.ini revision --autogenerate
alembic -c /code/src/shared/infrastructure/persistence/alembic.ini upgrade head
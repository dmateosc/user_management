#!/bin/sh


alembic -c /code/src/context/shared/infrastructure/persistence/alembic.ini revision --autogenerate
alembic -c /code/src/context/shared/infrastructure/persistence/alembic.ini upgrade head
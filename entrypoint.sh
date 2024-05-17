#!/bin/sh

# Ejecuta las migraciones de alembic
./create_alembic.sh

# Inicia el servidor Uvicorn
exec uvicorn src.main:app --host 0.0.0.0 --port 80 --reload

from fastapi import FastAPI
from context.user.infrastructure.app.rest.create_user.create_user import router as create_user
import os
from alembic import op

app = FastAPI()

app.include_router(create_user)


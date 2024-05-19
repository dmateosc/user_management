from fastapi import FastAPI

from app.rest.create_user.create_user import create_user
from app.rest.find_user.find_user import find_user

app = FastAPI()


app.include_router(create_user.router, prefix="/user", tags=["user"])
app.include_router(find_user.router, prefix="/user", tags=["user"])

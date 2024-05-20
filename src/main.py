from fastapi import FastAPI
from context.user.infrastructure.app.rest.routes_user import router as user_router
app = FastAPI()
app.include_router(user_router, prefix="/user")
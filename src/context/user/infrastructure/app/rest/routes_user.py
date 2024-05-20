from fastapi import APIRouter

from context.user.infrastructure.app.rest.create_user.create_user import router as create_user 
from context.user.infrastructure.app.rest.find_user.find_user import router as  find_user

router = APIRouter()



router.include_router(create_user, tags=["user"])
router.include_router(find_user, tags=["user"])

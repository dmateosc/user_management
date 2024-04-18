from fastapi import APIRouter, Depends
from model.user import UserRequest
from application.create.create_user import CreateUser
from apps.dependency_injection.user_config import get_user_repository
from user.application.model.user import UserDTO
router = APIRouter()

@router.post("/create")
def create_user(user: UserRequest, createUser: CreateUser = Depends(CreateUser(get_user_repository))):
  return createUser.create_user(userDTO=UserDTO().fromRequest(user)), 200

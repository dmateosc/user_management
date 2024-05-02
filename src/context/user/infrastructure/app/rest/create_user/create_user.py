from fastapi import APIRouter, Depends
from context.user.infrastructure.app.rest.model.user import UserRequest
from context.user.application.create.create_user import CreateUser
from apps.dependency_injection.user_config import get_user_repository
from context.user.application.model.user import UserDTO
router = APIRouter()

def create_user(user_repository =Depends(get_user_repository)):
  return CreateUser(user_repository)


@router.post("/create")
def user(user: UserRequest, createUser: CreateUser = Depends(create_user)):
  return createUser.save(userDTO=UserDTO.fromRequest(user)), 200

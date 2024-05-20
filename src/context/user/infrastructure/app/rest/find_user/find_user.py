from fastapi import APIRouter, Depends
from context.user.infrastructure.app.rest.model.user import UserResponse
from apps.dependency_injection.user_config import get_user_repository
from context.user.application.find_all.get_users import GetUsers
from context.user.application.find.get_user import GetUser


router = APIRouter()

def find_user(user_repository =Depends(get_user_repository)):
  return GetUser(user_repository)


def find_all(user_repository =Depends(get_user_repository)):
  return GetUsers(user_repository)


@router.get("/{dni}")
def find_user(dni = str, getUser: GetUser = Depends(find_user)):
  user = getUser.getUser(dni=dni)
  return user.toResponse(user)

@router.get("/")
def find_users(getUsers: GetUsers = Depends(find_all)):
  return getUsers.find_all()
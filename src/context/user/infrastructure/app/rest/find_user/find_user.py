from fastapi import APIRouter, Depends
from app.rest.model.user import UserResponse
from apps.dependency_injection.user_config import get_user_repository
from user.application.find_all.get_users import GetUsers
from user.application.find.get_user import GetUser


router = APIRouter()

def find_user(user_repository =Depends(get_user_repository)):
  return GetUser(user_repository)


def find_all(user_repository =Depends(get_user_repository)):
  return GetUsers(user_repository)


@router.get("/{user_id}")
def find_user(user_id = str, getUser: GetUser = Depends(find_user)):
  user = getUser.getUser(user_id=user_id)
  return UserResponse(
    name=user.name,
    last_date=user.last_date,
    last_name=user.last_name,
    active=user.active
  ), 200

@router.get("/")
def find_users(getUsers: GetUsers = Depends(find_all)):
  return getUsers.find_all()
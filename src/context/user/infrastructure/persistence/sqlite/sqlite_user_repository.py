from fastapi import Depends
from requests import Session
from domain.repository.user_repository import UserRepository
from domain.models.user import User
from sqlite.entity.user_entity import UserEntity
from sqlite_user_repository_factory import get_db

class SqliteUserRepository(UserRepository):
  def __init__(self) -> None:
    super().__init__()
  
  def save(self, user: User, db: Session = Depends(get_db)):
    userData = UserEntity().fromDomain(user=user)
    db.add(userData)
    db.commit()
    db.refresh(userData)
    
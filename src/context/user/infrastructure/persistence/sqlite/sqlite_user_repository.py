from fastapi import Depends
from sqlalchemy.orm import Session
from context.user.domain.repository.user_repository import UserRepository
from context.user.domain.models.user import User
from context.user.infrastructure.persistence.sqlite.entity.user_entity import UserEntity
from context.user.infrastructure.persistence.sqlite.sqlite_user_repository_factory import get_db


class SqliteUserRepository(UserRepository):
  def __init__(self) -> None:
    super().__init__()
  
  def save(user: User):
    db = get_db()
    userData = UserEntity().fromDomain(user=user)
    db.add(userData)
    db.commit()
    db.refresh(userData)
    
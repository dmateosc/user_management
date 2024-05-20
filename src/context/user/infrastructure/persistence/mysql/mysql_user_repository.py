from typing import List
from context.user.domain.repository.user_repository import UserRepository
from context.user.domain.models.user import User
from context.user.infrastructure.persistence.entity.user_entity import UserEntity
from context.user.infrastructure.persistence.mysql.mysql_user_repository_factory import get_db


class MySQLUserRepository(UserRepository):
  def __init__(self) -> None:
    super().__init__()
  
  def save(user: User):
    db = get_db()
    userData = UserEntity().fromDomain(user=user)
    db.add(userData)
    db.commit()
    db.refresh(userData)
  
  def find_all() -> List[User]:
    db = get_db()
    users = db.query(UserEntity).all()
    print(f"esto es un user: {users}")
    return [user.toDomain() for user in users]
  
  def find_user(dni: str) -> User:
    db = get_db()
    user = db.query(UserEntity).filter(UserEntity.dni == dni).first()
    print(f"esto es un user: {user}")
    return UserEntity.toDomain(user)
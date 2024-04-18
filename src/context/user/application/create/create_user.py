

from user.domain.repository.user_repository import UserRepository
from user.application.model.user import UserDTO


class CreateUser():
  def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
  def create_user(self, userDTO: UserDTO):
    return self.user_repository.save(
      UserDTO().toDomain(userDTO)
    )
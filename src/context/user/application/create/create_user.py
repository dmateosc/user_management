

from context.user.domain.repository.user_repository import UserRepository
from context.user.application.model.user import UserDTO


class CreateUser():
  def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        
  def save(self, userDTO: UserDTO):
    user = UserDTO.toDomain(userDTO)
    return self.user_repository.save(
      user=user
    )
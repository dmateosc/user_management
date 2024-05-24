

from context.user.application.model.user import UserDTO
from context.user.domain.repository.user_repository import UserRepository
from context.user.domain.models.user import DNI


class GetUser():
  def __init__(self, user_repository: UserRepository):
    self.user_repository = user_repository
  def getUser(self, dni: str) -> UserDTO:
    return UserDTO.fromDomain(self.user_repository.find_user(DNI(dni)))
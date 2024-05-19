

from user.application.model.user import UserDTO
from user.domain.repository.user_repository import UserRepository


class GetUser():
  def __init__(self, user_repository: UserRepository):
    self.user_repository = user_repository
  def getUser(self, user_id: str) -> UserDTO:
    return self.user_repository.find_by_id(user_id)
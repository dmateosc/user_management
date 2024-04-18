

from user.application.model.user import UserDTO
from user.domain.repository.user_repository import UserRepository


class GetUser():
  def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
  def getUser():
    return 
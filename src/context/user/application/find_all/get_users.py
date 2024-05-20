

from typing import List
from context.user.application.model.user import UserDTO
from context.user.domain.repository.user_repository import UserRepository


class GetUsers():
  def __init__(self, user_repository: UserRepository) -> List[UserDTO]:
    self.user_repository = user_repository
  def find_all(self):
    return  [UserDTO.fromDomain(user) for user in self.user_repository.find_all()]
 
from abc import ABC, abstractmethod
from typing import List
from context.user.domain.models.user import DNI, User

class UserRepository(ABC):
    @abstractmethod
    def save(user: User):
        pass
    @abstractmethod
    def find_all() -> List[User]:
        pass
    @abstractmethod
    def find_user(dni: DNI) -> User:
        pass
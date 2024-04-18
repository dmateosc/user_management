from abc import ABC, abstractmethod
from domain.models.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User):
        pass
    @abstractmethod
    def search(self):
        pass
    @abstractmethod
    def find_user(self):
        pass
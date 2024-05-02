from abc import ABC, abstractmethod
from context.user.domain.models.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(user: User ):
        pass
    @abstractmethod
    def search():
        pass
    @abstractmethod
    def find_user():
        pass
import pytest
from unittest.mock import MagicMock
from datetime import datetime

from context.user.application.create.create_user import CreateUser
from context.user.application.model.user import UserDTO
from context.user.domain.repository.user_repository import UserRepository

@pytest.fixture
def user_repository():
    return MagicMock(UserRepository)

@pytest.fixture
def create_user(user_repository):
    return CreateUser(user_repository)

def test_save_user(create_user, user_repository):
    # Arrange
    userDTO = UserDTO(
        name="John",
        last_name="Doe",
        phone=123456789,
        active=True,
        last_date=datetime.now()
    )
    user = MagicMock()
    UserDTO.toDomain = MagicMock(return_value=user)
    
    # Act
    create_user.save(userDTO)
    
    # Assert
    UserDTO.toDomain.assert_called_once_with(userDTO)
    user_repository.save.assert_called_once_with(user=user)


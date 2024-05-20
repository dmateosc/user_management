import pytest
from unittest.mock import MagicMock
from datetime import datetime
from context.user.application.find.get_user import GetUser
from context.user.application.model.user import UserDTO
from context.user.domain.repository.user_repository import UserRepository

@pytest.fixture
def user_repository():
    return MagicMock(UserRepository)

@pytest.fixture
def get_user_service(user_repository):
    return GetUser(user_repository)

def test_get_user(get_user_service, user_repository):
    # Arrange
    dni = "12345678X"
    domain_user = MagicMock()
    domain_user.first_name = "John"
    domain_user.last_name = "Doe"
    domain_user.phone_number = 123456789
    domain_user.is_active = True
    domain_user.last_login = datetime.now()
    
    user_repository.find_user.return_value = domain_user
    
    expected_user_dto = UserDTO(
        dni=domain_user.dni,
        name=domain_user.first_name,
        last_name=domain_user.last_name,
        phone=domain_user.phone_number,
        active=domain_user.is_active,
        last_date=domain_user.last_login
    )
    
    UserDTO.fromDomain = MagicMock(return_value=expected_user_dto)

    # Act
    user_dto = get_user_service.getUser(dni)
    
    # Assert
    user_repository.find_user.assert_called_once_with(dni)
    UserDTO.fromDomain.assert_called_once_with(domain_user)
    assert user_dto == expected_user_dto

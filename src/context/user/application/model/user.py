from datetime import datetime

from infrastructure.app.rest.create_user.model.user import UserRequest, UserResponse
from domain.models.user import Active, LastDate, Name, Phone, User

class UserDTO():
  def __init__(self, name: str, last_name: str, phone: int, active: bool, last_date: datetime):
    self.name = name
    self.last_name = last_name
    self.phone = phone
    self.active = active
    self.last_date = last_date
  
  @staticmethod
  def fromRequest(userRequest: UserRequest):
    return UserDTO(
      name=userRequest.name,
      last_name=userRequest.last_name,
      phone=userRequest.phone,
      last_date=userRequest.last_date,
      active=userRequest.active
    )
  @staticmethod 
  def toResponse(userDTO: 'UserDTO'):
    return UserResponse(
      name=userDTO.name,
      last_name=userDTO.last_name,
      phone=userDTO.phone,
      last_date=userDTO.last_date,
      active=userDTO.active
    )
  @staticmethod
  def toDomain(userDTO: 'UserDTO'):
    return User(
      name=Name(userDTO.name,userDTO.last_name),
      phone=Phone(userDTO.phone),
      last_date=LastDate(userDTO.last_date),
      active=Active(userDTO.active)
    )
    
  def fromDomain(user: User):
    return UserDTO(
      name=user.name.first_name,
      phone=user.phone.number,
      last_date=user.last_date.last_date,
      last_name=user.name.last_name,
      active=user.active.active

    )
      
  
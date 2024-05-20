from datetime import datetime

from context.user.infrastructure.app.rest.model.user import UserRequest, UserResponse
from context.user.domain.models.user import *

class UserDTO():
  def __init__(self,dni: str, name: str, last_name: str, phone: int, active: bool, last_date: datetime):
    self.dni = dni
    self.name = name
    self.last_name = last_name
    self.phone = phone
    self.active = active
    self.last_date = last_date
  
  @staticmethod
  def fromRequest(userRequest: UserRequest):
    return UserDTO(
      dni=userRequest.dni,
      name=userRequest.name,
      last_name=userRequest.last_name,
      phone=userRequest.phone,
      last_date=userRequest.last_date,
      active=userRequest.active
    )
  @staticmethod 
  def toResponse(user: 'UserDTO'):
    return UserResponse(
      dni= user.dni,
      name=user.name,
      last_name=user.last_name,
      phone=user.phone,
      last_date=user.last_date.strftime('%Y-%m-%d'),
      active=user.active
    )
  @staticmethod
  def toDomain(self):
    return User(
      dni=DNI(self.dni),
      name=Name(self.name,self.last_name),
      phone=Phone(self.phone),
      last_date=LastDate(self.last_date),
      active=Active(self.active)
    )
  @staticmethod
  def fromDomain(user: User):
    return UserDTO(
      dni=user.dni.dni,
      name=user.name.first_name,
      phone=user.phone.number,
      last_date=user.last_date.last_date,
      last_name=user.name.last_name,
      active=user.active.active

    )
      
  
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from context.user.domain.models.user import *
from context.shared.infrastructure.persistence.migration.models.base import Base
from datetime import datetime


class UserEntity(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  dni = Column(String(9), index=True) 
  name = Column(String(255), index=True)  # Specify length for VARCHAR
  last_name = Column(String(255), index=True)  # Specify length for VARCHAR
  phone = Column(Integer, index=True)
  active = Column(Boolean, index=True)
  last_date = Column(DateTime, index=True)
  
  @staticmethod
  def fromDomain(user: User):
    return UserEntity(
      dni=user.dni.dni,
      name=user.name.first_name,
      last_name=user.name.last_name,
      active=user.active.active,
      phone=user.phone.number,
      last_date=user.last_date.last_date
    )
  
  def toDomain(self):
    return User(
      dni=DNI(self.dni),
      name=Name(self.name,self.last_name),
      active=Active(self.active),
      phone=Phone(self.phone),
      last_date=LastDate(datetime.strftime(self.last_date,'%Y-%m-%d'))
    )
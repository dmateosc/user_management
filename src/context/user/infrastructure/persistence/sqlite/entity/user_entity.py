from sqlalchemy import Boolean, Column, DateTime, Integer, String
from context.user.domain.models.user import User

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UserEntity(Base):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, index=True)
  last_name = Column(String, index=True)
  phone = Column(Integer, index=True)
  active = Column(Boolean, index=True)
  last_date = Column(DateTime, index=True)
  @staticmethod
  def fromDomain(user: User):
    return UserEntity(
      name=user.name.first_name,
      last_name=user.name.last_name,
      active=user.active.active,
      phone=user.phone.number,
      last_date=user.last_date.last_date
    )
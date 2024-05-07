

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    event,
)
from sqlalchemy.orm import registry, relationship

from context.user.infrastructure.entity.user_entity import UserEntity
metadata = MetaData()
mapper_registry = registry(metadata=metadata)

users = UserEntity
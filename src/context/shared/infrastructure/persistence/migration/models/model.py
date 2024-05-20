from sqlalchemy.orm import registry

from context.shared.infrastructure.persistence.migration.models.base import Base
from context.user.infrastructure.persistence.entity.user_entity import UserEntity
metadata = Base.metadata
mapper_registry = registry(metadata=metadata)

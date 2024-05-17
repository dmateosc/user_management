



from sqlalchemy.orm import registry

from shared.infrastructure.persistence.migration.models.base import Base

metadata = Base.metadata
mapper_registry = registry(metadata=metadata)

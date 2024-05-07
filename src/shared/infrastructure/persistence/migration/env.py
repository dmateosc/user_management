from logging.config import fileConfig

from alembic import context
import os
import yaml

from shared.infrastructure.persistence.migration.models import model
from shared.infrastructure.persistence.mysql.mysql_config import create_mysql_config


environment = os.getenv("ENV",default="development")
config_file_path = f"{os.getcwd()}/config/config-{environment}.yml"

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
engine, SessionLocal, db_url = create_mysql_config()
# Define la URL de conexión a la base de datos SQLite
config.set_main_option('sqlalchemy.url',db_url)

target_metadata = model.metadata


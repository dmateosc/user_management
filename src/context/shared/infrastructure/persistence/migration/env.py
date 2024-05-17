from logging.config import fileConfig

from alembic import context
import os
import yaml

from shared.infrastructure.persistence.migration.models import model
from shared.infrastructure.persistence.mysql.mysql_config import create_mysql_config
from shared.infrastructure.utils.read_yaml import load_config



environment = os.getenv("ENV",default="development")
config_file_path = f"{os.getcwd()}/config/config-{environment}.yml"

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

config_yaml = load_config(config_file_path)
if config_yaml['database']['active'] == 'mysql':
    engine, SessionLocal, db_url = create_mysql_config()
    
# Define la URL de conexión a la base de datos SQLite
config.set_main_option('sqlalchemy.url',db_url)

target_metadata = model.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine

    with connectable.connect() as connection:
        print(f"esto es una conexión {engine}")
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()
            
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
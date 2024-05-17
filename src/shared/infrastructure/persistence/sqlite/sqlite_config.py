import yaml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

from shared.infrastructure.utils.read_yaml import load_config

# Obtener la ruta del directorio del script en ejecución
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo de configuración YAML
config_file_path = f"{os.getcwd()}/config/config-{os.getenv('ENV', 'development')}.yml"



def create_sqlite_config():
    config= load_config(config_file_path)

    db_file = config["database"]["database_file"]
    engine_kwargs ={}

    # Define la URL de conexión a la base de datos SQLite
    db_url = f"sqlite:///{db_file}"

    # Crea un objeto de motor SQLAlchemy con los argumentos adicionales proporcionados
    engine = create_engine(db_url, **engine_kwargs)

    # Crea una sesión de SQLAlchemy
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    return engine, SessionLocal

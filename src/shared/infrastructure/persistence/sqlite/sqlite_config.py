import yaml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Obtener la ruta del directorio del script en ejecución
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta al archivo de configuración YAML
config_file_path = os.path.join(script_dir, "sqlite-database-config.yaml")



def create_sqlite_config():
    with open(config_file_path, "r") as f:
        config = yaml.safe_load(f)

    db_file = config["database"]["database_file"]
    engine_kwargs ={}

    # Define la URL de conexión a la base de datos SQLite
    db_url = f"sqlite:///{db_file}"

    # Crea un objeto de motor SQLAlchemy con los argumentos adicionales proporcionados
    engine = create_engine(db_url, **engine_kwargs)

    # Crea una sesión de SQLAlchemy
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    return engine, SessionLocal

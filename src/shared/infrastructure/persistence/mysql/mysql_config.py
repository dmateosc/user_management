import yaml
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Obtener la ruta del directorio del script en ejecución

# Construir la ruta al archivo de configuración YAML

config_file_path = f"{os.getcwd()}/config/config-{os.getenv('ENV', 'development')}.yml"


def create_mysql_config():
    with open(config_file_path, "r") as f:
        config = yaml.safe_load(f)

    url = config["database"]["mysql"]["url"]
    user = config["database"]["mysql"]["user"]
    password = config["database"]["mysql"]["password"]
    database = config["database"]["mysql"]["database"]
    port = config["database"]["mysql"]["port"]
    engine_kwargs ={}

    # Define la URL de conexión a la base de datos SQLite
    db_url = f"mysql+mysqlconnector://{user}:{password}@{url}:{port}/{database}"

    # Crea un objeto de motor SQLAlchemy con los argumentos adicionales proporcionados
    engine = create_engine(db_url, **engine_kwargs)

    # Crea una sesión de SQLAlchemy
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    return engine, SessionLocal, db_url

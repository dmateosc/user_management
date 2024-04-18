import yaml
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def create_sqlite_config(config_file: str):
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    db_file = config["database"]["db_file"]
    engine_kwargs = config["database"]["engine_kwargs"]

    # Define la URL de conexión a la base de datos SQLite
    db_url = f"sqlite:///{db_file}"

    # Crea un objeto de motor SQLAlchemy con los argumentos adicionales proporcionados
    engine = create_engine(db_url, **engine_kwargs)

    # Crea una sesión de SQLAlchemy
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Crea una clase base declarativa para que todos los modelos se basen en ella
    Base = declarative_base()

    return engine, SessionLocal, Base

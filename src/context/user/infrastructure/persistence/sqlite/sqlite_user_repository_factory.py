from shared.infrastructure.persistence.sqlite.sqlite_config import create_sqlite_config

def get_db():
  SessionLocal = create_sqlite_config("config.yml")
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
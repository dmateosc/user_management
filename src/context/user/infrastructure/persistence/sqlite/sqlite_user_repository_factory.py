from shared.infrastructure.persistence.sqlite.sqlite_config import create_sqlite_config

def get_db():
  engine, SessionLocal, db_url = create_sqlite_config()
  db = SessionLocal()
  try:
      return db
  finally:
      db.close()
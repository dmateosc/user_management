from shared.infrastructure.persistence.mysql.mysql_config import create_mysql_config

def get_db():
  engine, SessionLocal = create_mysql_config()
  db = SessionLocal()
  try:
      return db
  finally:
      db.close()
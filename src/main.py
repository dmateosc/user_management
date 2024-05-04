from fastapi import FastAPI
from context.user.infrastructure.app.rest.create_user.create_user import router as create_user
import os
from alembic import op

app = FastAPI()

def execute_sql_scripts():
  migrations_folder = os.path.join(os.getcwd(), 'assets', 'db')
  for filename in os.listdir(migrations_folder):
      if filename.endswith('.sql'):
          filepath = os.path.join(migrations_folder, filename)
          with open(filepath) as file:
            op.execute(file.read())

app.include_router(create_user)

@app.on_event("startup")
async def startup_event():
    execute_sql_scripts()
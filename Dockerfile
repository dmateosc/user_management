# Usa la imagen oficial de Python como base
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el contenido del directorio actual al contenedor en /app
COPY . .

# Especifica el comando para ejecutar tu aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


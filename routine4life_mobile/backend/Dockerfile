# Usamos una versión específica y estable de Debian (Bookworm)
FROM python:3.11-slim-bullseye

# Instalar dependencias, la clave de MS con el método moderno y el driver ODBC
RUN apt-get update \
    && apt-get install -y curl gnupg2 apt-transport-https unixodbc-dev \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl -fsSL https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instala las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente al contenedor
COPY . .

# Expone el puerto que usará FastAPI
EXPOSE 8000

# Comando para iniciar el servidor
CMD ["uvicorn", "routine4life_mobile.backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
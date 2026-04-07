FROM python:3.12-slim

WORKDIR /app

# Instalar dependencias del sistema y el driver de SQL Server (ODBC 18)
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    unixodbc-dev \
    gcc \
    g++ \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl -fsSL https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el requirements que está en la carpeta padre (routine4life_web)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exponemos el puerto 8080 para que no choque con el 8000 de la app móvil
EXPOSE 8080

# Comando para ejecutar FastAPI. Asume que en main.py hay una variable llamada 'app'
CMD ["uvicorn", "miAPI.main:app", "--host", "0.0.0.0", "--port", "8080"]
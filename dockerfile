FROM python:3.11

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        gnupg2 \
        gcc \
        g++ \
        unixodbc-dev && \
    curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /usr/share/keyrings/microsoft-prod.gpg && \
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft-prod.gpg] https://packages.microsoft.com/ubuntu/22.04/prod jammy main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17 && \
    apt-get clean

WORKDIR /app

COPY routine4life_web/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY routine4life_web/ ./routine4life_web/
COPY miAPI/ ./miAPI/
COPY shared/ ./shared/

ENV PYTHONPATH=/app

EXPOSE 5000

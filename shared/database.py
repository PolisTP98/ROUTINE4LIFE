import os
import urllib.parse 
from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from sqlalchemy.engine import URL

load_dotenv()

server   = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
user     = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
driver   = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

DATABASE_URL = (
    f"mssql+pyodbc://{user}:{password}@{server}/{database}"
    f"?driver={driver.replace(' ', '+')}"
)

# Engine
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True

)

# Base
Base = declarative_base()

#Sesiones
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Función para obtener sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
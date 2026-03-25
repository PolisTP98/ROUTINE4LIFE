# shared/database.py
import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Credenciales
DB_SERVER = os.getenv("DB_SERVER", "DESKTOP-6RRSB8S\\SQLEXPRESS01")
DB_NAME = os.getenv("DB_NAME", "routine4life")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

# Para autenticación Windows (Trusted_Connection)
DATABASE_URL = (
    f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}"
    f"?driver={DB_DRIVER.replace(' ', '+')}"
    f"&trusted_connection=yes"
)

print(f"Conectando a: {DB_SERVER}/{DB_NAME}")

# Crear el motor
engine = create_engine(
    DATABASE_URL, 
    echo=False,
    pool_pre_ping=True,
)

# Base para modelos
Base = declarative_base()

# Fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Dependencia para obtener sesión de BD"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
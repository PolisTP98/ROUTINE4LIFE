import os
from pathlib import Path
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#URL de conexión 
DATABASE_URL = r"mssql+pyodbc://@DESKTOP-AUEI0C4\SQLEXPRESS01/routine4life?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

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
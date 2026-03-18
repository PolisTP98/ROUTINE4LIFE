# ----------------------------
# | IMPORTACIONES NECESARIAS |
# ----------------------------

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# ----------------------------------------------------
# | CARGAR LAS VARIABLES DE ENTORNO DEL ARCHIVO .env |
# ----------------------------------------------------

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path = env_path)

# OBTENER CREDENCIALES
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

if not all([DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD]):
    raise ValueError("FALTAN VARIABLES DE ENTORNO REQUERIDAS EN EL ARCHIVO .env")


# -----------------------------------------------------
# | CONFIGURACIÓN PARA LOS MODELOS ORM CON SQLAlchemy |
# -----------------------------------------------------

# CONSTRUIR EL URL DE LA CONEXIÓN PARA SQLAlchemy + pyodbc
DATABASE_URL = (
    f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
    f"?driver={DB_DRIVER.replace(' ', '+')}"
)

# CREAR EL MOTOR (engine)
engine = create_engine(
    DATABASE_URL, 
    echo = False, # NO VER LAS CONSULTAS SQL EN CONSOLA
    pool_pre_ping = True, # VERIFICAR LA CONEXIÓN ANTES DE USARLA (PARA EVITAR ERRORES POR CONEXIONES CAÍDAS)
)

# CREAR LA CLASE BASE PARA LOS MODELOS ORM DE SQLAlchemy
Base = declarative_base()

# CREAR LA FÁBRICA DE SESIONES
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

# DEPENDENCIA PARA OBTENER LA SESIÓN DE LA BD Y CERRARLA AUTOMÁTICAMENTE
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
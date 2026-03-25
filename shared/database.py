# ----------------------------
# | IMPORTACIONES NECESARIAS |
# ----------------------------

import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# ----------------------------------------------------
# | CARGAR LAS VARIABLES DE ENTORNO DEL ARCHIVO .env |
# ----------------------------------------------------

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path = env_path)

# OBTENER CREDENCIALES (Sin usuario ni contraseña porque usamos Windows Authentication)
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 17 for SQL Server")

# VALIDAR QUE EXISTAN LAS VARIABLES MÍNIMAS
if not all([DB_SERVER, DB_NAME]):
    raise ValueError("FALTAN VARIABLES DE ENTORNO REQUERIDAS EN EL ARCHIVO .env (DB_SERVER o DB_NAME)")


# -----------------------------------------------------
# | CONFIGURACIÓN PARA LOS MODELOS ORM CON SQLAlchemy |
# -----------------------------------------------------

# CONSTRUIR EL URL DE LA CONEXIÓN PARA SQLAlchemy + pyodbc (Con Conexión de Confianza)
DATABASE_URL = (
    f"mssql+pyodbc://{DB_SERVER}/{DB_NAME}"
    f"?driver={DB_DRIVER.replace(' ', '+')}"
    f"&Trusted_Connection=yes"
)

# CREAR EL MOTOR (engine)
engine = create_engine(
    DATABASE_URL, 
    echo = False, # NO VER LAS CONSULTAS SQL EN CONSOLA
    pool_pre_ping = True, # VERIFICAR LA CONEXIÓN ANTES DE USARLA
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
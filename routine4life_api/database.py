# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

import urllib.parse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# IMPORTAR LOGGER "db_logger"
from logger import db_logger

# IMPORTAR PARÁMETROS DE CONEXIÓN DE "config.py"
from config import(
    DRIVER, 
    SERVER, 
    DATABASE, 
    USERNAME, 
    PASSWORD, 
    TRUST_SERVER_CERTIFICATE
)


# ------------------------------------------
# | PREPARAR CREDENCIALES PARA LA CONEXIÓN |
# ------------------------------------------

# VALIDAR QUE "USERNAME" Y "PASSWORD" EXISTAN
# PYLANCE PIENSA QUE SON DEL TIPO DE DATO "str" O "None"
# "urllib.parse.quote_plus()" EXIGE TEXTO ("str"), NO "None"
assert USERNAME and PASSWORD

# CODIFICAR USUARIO Y CONTRASEÑA (CARACTERES ESPECIALES)
username = urllib.parse.quote_plus(USERNAME)
password = urllib.parse.quote_plus(PASSWORD)


# ----------------------------
# | CREAR CADENA DE CONEXIÓN |
# ----------------------------

connection_string = (
    f"mssql+pyodbc://{username}:{password}"
    f"@{SERVER}/{DATABASE}"
    f"?driver={DRIVER}"
    f"&TrustServerCertificate={'yes' if TRUST_SERVER_CERTIFICATE else 'no'}"
)
db_logger.info("SQLALCHEMY CONNECTION STRING CREATED")


# -------------------
# | CREAR MOTOR ORM |
# -------------------

engine = create_engine(
    connection_string, 
    fast_executemany = True, 
    echo = False, 
    pool_size = 10, 
    max_overflow = 20, 
    pool_timeout = 30, 
    pool_pre_ping = True, 
    execution_options = {"isolation_level": "READ COMMITTED"}
)
db_logger.info("SQLALCHEMY ENGINE INITIALIZED")


# -----------------------------------------
# | CREAR CLASE BASE PARA LOS MODELOS ORM |
# -----------------------------------------

Base = declarative_base()
db_logger.info("SQLALCHEMY BASE READY")


# -------------------------------------------
# | CREAR FÁBRICA DE SESIONES DE BASE DATOS |
# -------------------------------------------

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)
db_logger.info("SQLALCHEMY SESSION FACTORY READY")


# ----------------------------------------------------
# | FUNCIÓN PARA CONSEGUIR Y LIBERAR UNA SESSION ORM |
# ----------------------------------------------------

def get_db():
    database = SessionLocal()
    try:
        yield database
    except Exception:
        database.rollback()
        db_logger.exception("UNEXPECTED DATABASE EXCEPTION")
        raise
    finally:
        database.close()
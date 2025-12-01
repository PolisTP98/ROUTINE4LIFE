# IMPORTAR MÓDULOS NECESARIOS
import os
import pyodbc
# CREA UN ARCHIVO .env EN LA RAÍZ DEL PROYECTO
from dotenv import load_dotenv

# ---------------------------------------
# | CONFIGURAR LA CONEXIÓN A SQL SERVER |
# ---------------------------------------

# CARGAR LAS VARIABLES DEL ARCHIVO .env
load_dotenv()

# PARÁMETROS DE LA CONEXIÓN DESDE .env
DRIVER = "{ODBC Driver 17 for SQL Server}"
SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_DATABASE")
USERNAME = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
TRUST_SERVER_CERTIFICATE = True

# CADENA DE CONEXIÓN
CONNECTION_STRING = (
    f"DRIVER={DRIVER};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    f"TrustServerCertificate={'yes' if TRUST_SERVER_CERTIFICATE else 'no'};"
)

def get_connection():
    # INTENTA CONECTARSE A LA BASE DE DATOS EN SQL SERVER
    # DEVUELVE LA CONEXIÓN SI ES EXITOSA
    # LANZA ConnectionError EN CASO DE FALLO
    try:
        connection = pyodbc.connect(CONNECTION_STRING, autocommit = True)
        return connection
    except pyodbc.Error as exception:
        raise ConnectionError(exception)
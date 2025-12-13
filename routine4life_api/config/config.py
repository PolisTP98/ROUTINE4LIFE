# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

import os
import pyodbc

# CREAR ARCHIVO ".env" EN LA RAÍZ DEL PROYECTO
from dotenv import load_dotenv

# IMPORTAR LOGGER "db_logger"
from logger import db_logger


# ------------------------------------
# | CONFIGURAR CONEXIÓN A SQL SERVER |
# ------------------------------------

# CARGAR VARIABLES DE ENTORNO DEL ARCHIVO ".env"
load_dotenv()

# PARÁMETROS DE CONEXIÓN DESDE EL ARCHIVO ".env"
DRIVER = f"{{{os.getenv(
    'DB_DRIVER', 
    'ODBC Driver 17 for SQL Server'
)}}}"
SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_DATABASE")
USERNAME = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
TRUST_SERVER_CERTIFICATE = (
    os.getenv(
        "DB_TRUST_SERVER_CERTIFICATE", 
        "false"
    )
    .strip()
    .lower() == "true"
)

# VALIDAR PARÁMETROS DE CONEXIÓN
required_variables = {
    "DB_SERVER": SERVER, 
    "DB_DATABASE": DATABASE, 
    "DB_USER": USERNAME, 
    "DB_PASSWORD": PASSWORD
}
missing_variables = [
    key for key, value in required_variables.items() if not value
]
if missing_variables:
    raise EnvironmentError(
        f"MISSING CONNECTION PARAMETERS: {', '.join(missing_variables)}"
    )

# CADENA DE CONEXIÓN
CONNECTION_STRING = (
    f"DRIVER={DRIVER};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    f"TrustServerCertificate={'yes' if TRUST_SERVER_CERTIFICATE else 'no'};"
)


# -------------------------------
# | HACER CONEXIÓN A SQL SERVER |
# -------------------------------

def get_connection(autocommit: bool = False):

    # INTENTAR CONECTARSE A LA BASE DE DATOS EN SQL SERVER
    # DEVOLVER CONEXIÓN SI ES EXITOSA
    # LANZAR ConnectionError SI FALLA
    try:
        db_logger.info("TRYING TO CONNECT TO SQL SERVER")
        connection = pyodbc.connect(
            CONNECTION_STRING, 
            autocommit = autocommit, 
            timeout = 10
        )
        db_logger.info("CONNECTION TO SQL SERVER ESTABLISHED")
        return connection
    except pyodbc.Error as exception:
        db_logger.exception("ERROR CONNECTING TO SQL SERVER")
        raise ConnectionError(
            "UNABLE TO ESTABLISH CONNECTION TO THE DATABASE"
        ) from exception
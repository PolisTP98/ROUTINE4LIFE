import pyodbc

# ------------------------------------------
# | CONFIGURACIÓN DE CONEXIÓN A SQL SERVER |
# ------------------------------------------

# PARÁMETROS DE LA CONEXIÓN
DRIVER = "{ODBC Driver 18 for SQL Server}"
SERVER = "POLISTP98"
DATABASE = "routine4life"
Trusted_Connection = True
Encrypt = True
TrustServerCertificate = True

# CADENA DE TEXTO DE CONEXIÓN
CONNECTION_STRING = (
    f"DRIVER={DRIVER};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection={'yes' if Trusted_Connection else 'no'};"
    f"Encrypt={'yes' if Encrypt else 'no'};"
    f"TrustServerCertificate={'yes' if TrustServerCertificate else 'no'};"
)

# FUNCIÓN PARA REALIZAR CONEXIÓN A LA BASE DE DATOS
def getConnection():
    try:
        connection = pyodbc.connect(CONNECTION_STRING)
        return connection
    except pyodbc.Error as exception:
        print(
            f"\n# AN ERROR OCCURRED WHILE ATTEMPTING TO CONNECT TO THE DATABASE:"
            f"\n{exception}"
            f"\n# CONNECTION STRING USED:"
            f"\n{CONNECTION_STRING}\n"
        )
        raise ConnectionError(exception)
import pyodbc

def config(
        DRIVER, 
        SERVER, 
        DATABASE, 
        Trusted_Connection, 
        Encrypt, 
        TrustServerCertificate):

    connection_str = f"""
DRIVER={{{DRIVER}}};
SERVER={SERVER};
DATABASE={DATABASE};
Trusted_Connection={'yes' if Trusted_Connection else 'no'};
Encrypt={'yes' if Encrypt else 'no'};
TrustServerCertificate={'yes' if TrustServerCertificate else 'no'};
""".strip()

    try:
        return pyodbc.connect(connection_str)
    except pyodbc.Error as e:
        raise ConnectionError(f"""
Error al conectar a la base de datos: {e}

Cadena de conexión utilizada:
{connection_str}
""")
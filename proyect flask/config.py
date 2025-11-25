import pyodbc

def Config(index):
    connections = [
        f"DRIVER={{ODBC Driver 18 for SQL Server}};"
        f"SERVER=DESKTOP-6RRSB8S\\SQLEXPRESS01;"
        f"DATABASE=routine4life;"
        f"Trusted_Connection=yes;"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes"
    ]
    
    if index not in range(len(connections)):
        raise IndexError("Índice de conexión fuera de rango")

    try:
        return pyodbc.connect(connection_str)
    except pyodbc.Error as e:
        raise ConnectionError(f"""
Error al conectar a la base de datos: {e}

Cadena de conexión utilizada:
{connection_str}
""")
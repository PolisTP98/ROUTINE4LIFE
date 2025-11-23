import pyodbc

def Config(index):
    connections = [
        f"DRIVER={{SQL Server}};"
        f"SERVER=IANDAVID\\SQLSERVER;"
        f"DATABASE=ROUTINE4LIFE_DB;"
        f"Trusted_Connection=yes;"
        f"Encrypt=yes;"
        f"TrustServerCertificate=yes"
    ]
    
    if index not in range(len(connections)):
        raise IndexError("Índice de conexión fuera de rango")

    try:
        connection = pyodbc.connect(connections[index])
        return connection
    except pyodbc.Error as e:
        raise ConnectionError(f"Error al conectar a la base de datos: {e}")
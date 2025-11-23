import pyodbc

def Config(index):
    connections = [
        f"DRIVER={{ODBC Driver 18 for SQL Server}};" 
        f"SERVER=DESKTOP-6RRSB8S\\SQLEXPRESS01;" 
        f"DATABASE=ROUTINE4LIFE_DB;"
        f"Trusted_Connection=yes"
    ]
    
    if index not in range(len(connections)):
        raise IndexError("Índice de conexión fuera de rango")

    try:
        connection = pyodbc.connect(connections[index])
        return connection
    except pyodbc.Error as e:
        raise ConnectionError(f"Error al conectar a la base de datos: {e}")
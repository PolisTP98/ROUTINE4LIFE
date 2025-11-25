from flask import Flask, jsonify
from config import getConnection

# -----------------------------------
# | INICIALIZACIÓN DE LA APLICACIÓN |
# -----------------------------------

app = Flask(__name__)


# -------------------
# | RUTAS DE LA API |
# -------------------

# VERIFICAR EL FUNCIONAMIENTO DE LA API Y LA CONEXIÓN A LA BASE DE DATOS
@app.route("/api/v0.0.0/connectionStatus", methods=["GET"])
def connectionStatus():
    try:
        connection = getConnection()
        # SI LA CONEXIÓN ES EXITOSA, LA CERRAMOS INMEDIATAMENTE
        connection.close()
        return jsonify({
            "status": "online",
            "database_connection": "successful",
            "message": "api and db ok"
        }), 200
    except ConnectionError as exception:
        # SI getConnection() LANZA UN ConnectionError (FALLO EN pyodbc.connect)
        return jsonify({
            "status": "online",
            "database_connection": "failed",
            "message": str(exception)
        }), 500


# --------------------------
# | EJECUCIÓN DEL SERVIDOR |
# --------------------------

if __name__ == '__main__':
    # USAMOS EL HOST '0.0.0.0' PARA QUE SEA ACCESIBLE DESDE EL AVD (10.0.2.2) 
    # Y DESDE LA RED LOCAL CON EL PUERTO 5000 POR DEFECTO
    print("Iniciando servidor Flask en http://0.0.0.0:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
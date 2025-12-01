# IMPORTAR MÓDULOS NECESARIOS
from flask import Flask, jsonify
from config import get_connection
from logger import setup_logger

# -----------------------------------------
# | INICIALIZAR LA APLICACIÓN Y EL LOGGER |
# -----------------------------------------

app = Flask(__name__)
logger = setup_logger()


# -------------------
# | RUTAS DE LA API |
# -------------------

# VERIFICAR EL FUNCIONAMIENTO DE LA API Y LA CONEXIÓN A LA BASE DE DATOS
@app.route("/api/v1/connection_status", methods = ["GET"])
def connection_status():
    try:
        logger.info("VERIFYING THE CONNECTION TO THE DATABASE")
        connection = get_connection()
        connection.close()
        logger.info("DATABASE CONNECTED SUCCESSFULLY")
        return jsonify({
            "status": "online",
            "database_connection": "successful",
            "message": "the api and database are working properly"
        }), 200
    except ConnectionError as exception:
        logger.error("DATABASE CONNECTION ERROR", exc_info = True)
        return jsonify({
            "status": "online",
            "database_connection": "failed",
            "message": str(exception)
        }), 500


# ------------------------
# | EJECUTAR EL SERVIDOR |
# ------------------------

if __name__ == '__main__':
    # SE USA EL HOST 0.0.0.0 PARA QUE SEA ACCESIBLE DESDE EL AVD (10.0.2.2) 
    # Y DESDE LA RED LOCAL CON EL PUERTO 5000 POR DEFECTO
    logger.info("STARTING FLASK SERVER ON http://0.0.0.0:5000")
    app.run(host = "0.0.0.0", port = 5000, debug = True)
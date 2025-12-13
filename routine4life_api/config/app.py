# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

from flask import Flask, jsonify

# IMPORTAR FUNCIÓN DE CONEXIÓN A SQL DE "config.py"
from config import get_connection

# IMPORTAR LOGGER "app_logger"
from logger import app_logger


# --------------------------
# | INICIALIZAR APLICACIÓN |
# --------------------------

app = Flask(__name__)


# -------------------
# | RUTAS DE LA API |
# -------------------

# VERIFICAR EL FUNCIONAMIENTO DE LA API Y LA CONEXIÓN A LA BASE DE DATOS
@app.route("/api/v1/connection_status", methods = ["GET"])
def connection_status():
    try:
        app_logger.info("VERIFYING THE CONNECTION TO THE DATABASE")
        with get_connection() as connection: pass
        app_logger.info("DATABASE CONNECTED SUCCESSFULLY")
        return jsonify({
            "status": "online",
            "database_connection": "successful",
            "message": "the api and database are working properly"
        }), 200
    except ConnectionError as exception:
        app_logger.exception("DATABASE CONNECTION ERROR")
        return jsonify({
            "status": "online",
            "database_connection": "failed",
            "message": str(exception)
        }), 500


# ------------------------
# | EJECUTAR EL SERVIDOR |
# ------------------------

if __name__ == '__main__':

    # USAR EL HOST 0.0.0.0 PARA QUE SEA ACCESIBLE DESDE EL AVD (10.0.2.2) 
    # TAMBIÉN DESDE LA RED LOCAL CON EL PUERTO 5000 POR DEFECTO
    app_logger.info("STARTING FLASK SERVER ON http://0.0.0.0:5000")
    app.run(host = "0.0.0.0", port = 5000, debug = True)
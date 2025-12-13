# -------------------------------
# | IMPORTAR MÓDULOS NECESARIOS |
# -------------------------------

import os
import logging
from logging.handlers import TimedRotatingFileHandler


# -----------------
# | CREAR LOGGERS |
# -----------------

# GUARDAR MENSAJES DE INFORMACIÓN Y ERROR DEL SISTEMA EN UN ARCHIVO ".log"
# TAMBIÉN MOSTRARLOS EN CONSOLA
def create_logger(
    name: str, 
    log_file: str, 
    log_dir: str = "storage/logs", 
    log_level = logging.INFO
    ):

    # CREAR CARPETAS SI NO EXISTEN
    os.makedirs(log_dir, exist_ok = True)

    # CREAR RUTA DE CADA ARCHIVO ".log"
    log_path = os.path.join(log_dir, log_file)
    logger = logging.getLogger(name)

    # ESTABLECER NIVEL DEL LOGGER
    logger.setLevel(log_level)

    # EVITA LOGS DUPLICADOS CON FLASK
    logger.propagate = False

    # EVITAR DUPLICAR HANDLERS
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # ARCHIVO (ROTACIÓN DIARIA)
        file_handler = TimedRotatingFileHandler(
            log_path, 
            when = "midnight", 
            interval = 1, 
            backupCount = 7, 
            encoding = "utf-8", 
            utc = False
        )
        file_handler.suffix = "%Y-%m-%d"
        file_handler.setFormatter(formatter)

        # CONSOLA
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # HANDLERS
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger


# ---------------------------
# | CREAR LOGGER POR MÓDULO |
# ---------------------------

db_logger = create_logger("db", "db.log")
api_logger = create_logger("api", "api.log")
app_logger = create_logger("app", "app.log")
auth_logger = create_logger("auth", "auth.log")
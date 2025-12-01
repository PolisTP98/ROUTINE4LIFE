# IMPORTAR MÓDULOS NECESARIOS
import os
import logging

# -----------------
# | CREAR LOGGERS |
# -----------------

# GUARDAR LOS MENSAJES DE INFORMACIÓN Y ERROR DEL SISTEMA EN UN ARCHIVO .log
# Y MOSTRARLOS EN LA CONSOLA
def create_logger(
    name: str,
    log_file: str,
    log_dir: str = "storage/logs",
    log_level = logging.INFO
    ):
    # CREAR CARPETAS SI NO EXISTEN
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.propagate = False

    # EVITAR DUPLICAR HANDLERS
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        # ARCHIVO
        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)

        # CONSOLA
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # HANDLERS
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger


# ------------------------------
# | CREAR UN LOGGER POR MÓDULO |
# ------------------------------

db_logger   = create_logger("db",   "db.log")
api_logger  = create_logger("api",  "api.log")
app_logger  = create_logger("app",  "app.log")
auth_logger = create_logger("auth", "auth.log")
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

_CONFIGURED = False


def configure_logging():
    """
    Configura logging global:
    - Consola + archivo
    - Rotación por tamaño
    """
    global _CONFIGURED
    if _CONFIGURED:
        return

    # Crear carpeta de logs
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "suite.log"

    # Logger raíz
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Formato del log
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 🟢 Handler de archivo con rotación (SIEMPRE se agrega)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000,   # ~1MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)

    # 🟢 Handler de consola (solo si no existe)
    if not any(isinstance(h, logging.StreamHandler) for h in root_logger.handlers):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

    _CONFIGURED = True


def get_logger(name: str):
    """
    Devuelve un logger listo para usar.
    """
    configure_logging()
    return logging.getLogger(name)

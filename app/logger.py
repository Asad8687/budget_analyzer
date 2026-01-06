import logging
from app.config import LOG_FILE

def get_logger():
    logger = logging.getLogger("budget")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(LOG_FILE)
        formatter = logging.Formatter("%(levelname)s: %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
# FORCE CHANGE TEST

import logging
from datetime import datetime

class CustomFormatter(logging.Formatter):
    FORMATS = {
        logging.DEBUG: "[%(asctime)s] 🐞 DEBUG → %(message)s",
        logging.INFO:  "[%(asctime)s] ✅ INFO  → %(message)s",
        logging.WARNING: "[%(asctime)s] ⚠️ WARNING → %(message)s",
        logging.ERROR: "[%(asctime)s] ❌ ERROR → %(message)s",
        logging.CRITICAL: "[%(asctime)s] 🚨 CRITICAL → %(message)s"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

def get_logger(name="my_logger", level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(CustomFormatter())
        logger.addHandler(handler)

    return logger

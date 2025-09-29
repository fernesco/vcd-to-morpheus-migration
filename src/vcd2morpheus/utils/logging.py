import logging, os

def setup_logger(name: str):
    lvl = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(level=getattr(logging, lvl), format="%(asctime)s %(levelname)s %(message)s")
    return logging.getLogger(name)

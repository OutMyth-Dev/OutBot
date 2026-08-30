import logging

from logging.handlers import TimedRotatingFileHandler

def custom_logger() -> None:

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename="discord.log", when="d", interval=7, backupCount=0
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

import logging

from logging.handlers import TimedRotatingFileHandler

def custom_logger() -> None:

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(
        filename="discord.log", encoding="utf-8", mode="a"
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    logging.handlers.TimedRotatingFileHandler(
        filename="discord.log", when="d", interval=7, backupCount=0
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

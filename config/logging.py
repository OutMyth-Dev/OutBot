import logging
from logging.handlers import TimedRotatingFileHandler


def custom_logger() -> None:
    """
    Creates a custom logger for OutBot to use.

    Args:
        None

    Returns:
        None
    """
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)

    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename="discord.log", when="d", interval=1, backupCount=1
    )

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

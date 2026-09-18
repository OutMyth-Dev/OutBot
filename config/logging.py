import logging
import os
from logging.handlers import TimedRotatingFileHandler


def delete_old_logs(current_log_file: str, old_log_file: str) -> None:
    """
    Deletes logs after a day instad of renaming them into year-month-date discord.log.

    Args:
        current_log_file: == discord.log
        old_log_file: == year-month-date discord.log

    Returns:
        None
    """
    os.remove(old_log_file)


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
        filename="discord.log",
        when="d",
        interval=1,
        backupCount=0,
    )

    file_handler.rotator = delete_old_logs

    formatter = logging.Formatter(
        "%(name)s | %(message)s",
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

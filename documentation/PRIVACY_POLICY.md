Logs are automatically deleted everyday. OutBot does **ONLY** logs error. OutBot **DOES NOT** log message content or other user info.

Users reports and feedback **are deleted as soon as they are dealt with appropriately.**

- Logs use a logging mode of **a** (append).

> This is how logging.py is configured.
```py
import logging
import os
from logging.handlers import TimedRotatingFileHandler


def delete_old_logs(current_log_file: str, _: str) -> None:
    """
    Deletes logs after a day instad of renaming them into year-month-date discord.log.

    Args:
        current_log_file: == discord.log
        _: == year-month-date discord.log

    Returns:
        None
    """
    os.remove(source)


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
        "%(asctime)s | %(name)s | %(message)s",
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
```


If you have any privacy concerns, please open a GitHub issue, create a ticket on OutMyth's discord server, or use /report.

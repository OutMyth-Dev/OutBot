Logs are automatically deleted everyday. OutBot does **NOT** only logs error. OutBot **DOES NOT** log message content or other user info.

Users reports and feedback **are deleted as soon as they are dealt with appropriately.**

- Logs use a logging mode of **a** (append).

> This is how logging.py is configured.
```text
import logging
from logging.handlers import TimedRotatingFileHandler


def custom_logger() -> None:

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
```

OutBot uses **NO** privileged intents. Therefore, intents=discord.Intents.default().

If you have any privacy concerns, please open a GitHub issue, create a ticket on OutMyth's discord server, or use /report.

# OutBot's Privacy Policy

----

## Logs

| Data | Data Collected | Stored | Retained |
| --- | --- | --- | --- |
| Message content | N/A | N/A | N/A |
| User data | N/A | N/A | N/A |
| Logs | Errors Only | Locally | Automatically deleted daily |

**OutBot only logs errors. Logs are deleted automatically everyday.**
```text
file_handler = logging.handlers.TimedRotatingFileHandler(
    filename="discord.log", when="d", interval=1, backupCount=0
)
```

- Logs use a logging mode of **a** (append)

This is how logging.py is configured.
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

---

# Privileged Intents

OutBot uses **NO** privileged intents. OutBot only uses discord's default intents.
```text
bot = OutBot(
    command_prefix=None,
    # Intents
    intents=discord.Intents.default(),
)
```

If you have any privacy concerns, please open a GitHub issue; create a ticket on OutMyth's discord server; /report; /feedback.

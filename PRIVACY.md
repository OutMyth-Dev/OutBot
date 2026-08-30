# OutBot's Privacy Policy

----

## 🗂️ Logs

| Data | Collected | Stored | Retention |
| --- | --- | --- | --- |
| Message content | ❌ No | ❌ No | None |
| User data | ❌ No | ❌ No | None |
| Logs | ✅ Limited | ✅ Local | 7 days |

**OutBot only logs errors. Logs are deleted automatically after 7 days.**
```text
file_handler = logging.handlers.TimedRotatingFileHandler(
    filename="discord.log", when="d", interval=7, backupCount=0
)
```


- Logs use a logging mode of **a** (append)
- OutBot is **open source**
- OutBot is under an MIT LICENSE: https://github.com/OutMyth-Dev/OutBot/blob/main/LICENSE

If you have any privacy concerns please open a GitHub issue or create a ticket on OutMyth's discord server.

THis is how logging.py is configured.

```text
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
```

---

# 👑 Privileged Intents

OutBot uses **NO** privileged intents. OutBot only uses discord's default intents (as shows in the code below).
```text
bot = OutBot(
    command_prefix=None,
    **intents=discord.Intents.default(),**
)
```


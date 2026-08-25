import logging

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(
    filename="discord.log",
    encoding="utf-8",
    mode="a",
)

formatter = logging.Formatter(
    "Time = %(asctime)s | File and dir name = %(name)s | Log Level = %(levelname)s | Who used command = %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

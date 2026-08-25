import logging

log_handler = logging.FileHandler(
    filename="discord.log",
    encoding="utf-8",
    mode="a",
)

log_level = logging.DEBUG

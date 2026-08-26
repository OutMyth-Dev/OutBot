import logging


def custom_logger() -> None:

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(
        filename="discord.log",
        encoding="utf-8",
        mode="a",
    )

    formatter = logging.Formatter(
        "Time = %(asctime)s   ||   Logger/Module Name = %(name)s   ||   Log Level = %(levelname)s   |   Your Messge = %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

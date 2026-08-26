import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from config.extensions import extensions
from config.logging import custom_logger

# Set Up Logger

custom_logger()

logger = logging.getLogger(__name__)

# Discord Configuration

load_dotenv("config/.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    logger.error("Discord token was not found.")
    raise RuntimeError(
        "Discord token not found. Please enter your Discord bot's token."
    )

# Load Cogs


class OutBot(commands.Bot):
    async def setup_hook(self) -> None:
        for extension in extensions:
            await self.load_extension(extension)


# Command Prefixes And Intents


bot = OutBot(
    command_prefix=None,
    intents=discord.Intents.default(),
)

# Events


@bot.event
async def on_ready() -> None:

    logger.info("OutBot can now be used.")

    commands_synced = await bot.tree.sync()

    logger.info(
        "Synced %d commands",
        len(commands_synced),
    )


# Bot Initialization


bot.run(
    DISCORD_TOKEN,
)

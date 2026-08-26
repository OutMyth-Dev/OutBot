import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from config.extensions import extensions
from config.logging import custom_logger
from config.prefixes import command_prefix

# Set Up Logger

custom_logger()

logger = logging.getLogger(__name__)

# Discord Configuration

load_dotenv("config/.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise RuntimeError("Discord token not found.\nPlease enter you Discod bot's token.")

# Load Cogs


class OutBot(commands.Bot):
    async def setup_hook(self):
        for extension in extensions:
            await self.load_extension(extension)


# Command Prefixes And Intents


bot = OutBot(
    command_prefix=command_prefix,
    intents=discord.Intents.default(),
)

# Events


@bot.event
async def on_ready():

    logger.info("OutBot is online.")

    commands_synced = await bot.tree.sync()

    logger.info(
        "Synced %d commands",
        len(commands_synced),
    )


# Bot Initialization


bot.run(
    DISCORD_TOKEN,
)

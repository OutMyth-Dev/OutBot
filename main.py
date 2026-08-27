import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from config.load_cogs import find_cogs
from config.logging import custom_logger

# Set Up Logger


custom_logger()
logger = logging.getLogger(__name__)

# Discord Configuration


load_dotenv("config/.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    logger.error("Discord token was not found.")
    raise RuntimeError("Bot Token Not Found.")

# Load Cogs & Syncing Commands


class OutBot(commands.Bot):
    async def setup_hook(self) -> None:
        for cog in find_cogs:
            if cog.endswith(".py"):
                await self.load_extension(f"cogs.{cog[:-3]}")

        commands_synced = await self.tree.sync()

        logger.info("OutBot can now be used.")
        logger.info(
            f"Synced commands {len(commands_synced)}",
        )


# Command Prefixes And Intents


bot = OutBot(
    command_prefix=None,
    intents=discord.Intents.default(),
)

# Bot Initialization


bot.run(DISCORD_TOKEN)

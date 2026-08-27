import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from config import custom_logger, find_cogs

custom_logger()
logger = logging.getLogger(__name__)

load_dotenv("config/.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    logger.error("Discord token was not found.")
    raise RuntimeError("Bot Token Not Found.")


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


bot = OutBot(
    command_prefix=None,
    intents=discord.Intents.default(),
)

bot.run(DISCORD_TOKEN)

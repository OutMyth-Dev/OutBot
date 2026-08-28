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


class OutBot(commands.Bot):
    async def setup_hook(self) -> None:

        for cog in find_cogs:
            if cog.endswith("cog.py"):
                await self.load_extension(f"cogs.{cog[:-3]}")

        commands_synced = await bot.tree.sync()

        logger.info("OutBot can now be used.")
        logger.info(f"Synced commands {len(commands_synced)}")


bot = OutBot(
    command_prefix=None,
    intents=discord.Intents.default(),
)


try:
    bot.run(DISCORD_TOKEN)
    logger.info(f"Logged in.")


except discord.LoginFailure:
    logger.critical("Please enter your Discord Bot's token.")
    raise RuntimeError("Bot Token could not be verfied.")

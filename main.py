import logging
import os


import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv


from config import custom_logger, find_cogs
from utils import send_error_message


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
        logger.info(f"OutBot is ready with {commands_synced} /commands.")
    
    async def on_app_command_error(
        self, 
        interaction: discord.Interaction,
        error: app_commands.AppCommandError
    ) -> None:

        embed_error_message = discord.Embed(
            title="Something went wrong.",
            description=(
                "An unexpected error occurred while running the command you used.",
                "This is NOT your fault.",
                "Please open a ticket."
            ),
            colour=0xe74c3c,
        )

        send_error_message(
            interaction, embed=embed_error_message
        )

        logger.WARNING(f"This error occuered when using a command: {error}")


bot = OutBot(
    command_prefix=None,
    intents=discord.Intents.default(),
)


try:
    bot.run(DISCORD_TOKEN)


except discord.LoginFailure:
    logger.CRITICAL("You entered an incorrect bot token.")
    raise RuntimeError("Invlaid bot token.")

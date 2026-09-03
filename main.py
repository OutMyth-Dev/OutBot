import logging
import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from config import custom_logger, find_cogs
from utils import error_message

custom_logger()
logger = logging.getLogger(__name__)


load_dotenv("config/.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


class OutBot(commands.Bot):
    async def setup_hook(self) -> None:

        for cog in find_cogs:
            if cog.endswith("cog.py"):
                # This line filters for "cog.py". This allows developers to add other files like __init__.py to the cogs directory.
                await self.load_extension(f"cogs.{cog[:-3]}")

        await bot.tree.sync()

    async def on_app_command_error(
        self, interaction: discord.Interaction, error: app_commands.AppCommandError
    ) -> None:

        embed_error_message = discord.Embed(
            title="Something went wrong. :(",
            description=(
                "An unexpected error occurred.\n",
                "Please create a ticket or open a GitHub issue.",
            ),
            colour=0xE74C3C,
        )

        error_message(interaction, embed=embed_error_message)
        logger.ERROR(f"Unexpected error: {error}")


bot = OutBot(
    command_prefix=None,
    intents=discord.Intents.default(),
)


try:
    bot.run(DISCORD_TOKEN)


except TypeError:
    raise RuntimeError(
        "Invlaid bot token. Please enter your discord bot token in a file called '.env' (you have to create it yourself) inside the folder 'config'.",
    )


except discord.LoginFailure:
    raise RuntimeError(
        "Invlaid bot token. Please enter your discord bot token in a file called '.env' (you have to create it yourself) inside the folder 'config'.",
    )

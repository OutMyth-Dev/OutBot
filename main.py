import logging
import os

import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from config import custom_logger
from utils import error_message

custom_logger()
logger = logging.getLogger(__name__)


load_dotenv("config/.env")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


class OutBot(commands.Bot):
    """
    Loads all cogs, contains centrelized error handling, and syncs all commands to the command tree.

    Attributes:
        None

    Methods:
        setup_hook: Loads all cogs and syncs all commands.
        on_app_command_error: Sends an embed when unexpected errors occur and logs them.
    """

    async def setup_hook(self) -> None:
        """
        Loads all cogs and syncs all commands to the command tree

        Args:
            None

        Returns:
            None
        """

        find_cogs = os.listdir("cogs")
        for cog in find_cogs:
            if cog.endswith("cog.py"):
                await self.load_extension(f"cogs.{cog[:-3]}")

        await self.tree.sync()

    async def on_app_command_error(
        self, interaction: discord.Interaction, error: app_commands.AppCommandError
    ) -> None:
        """
        Sends an embed when unexpected errors occur.

        Args:
            interaction (discord.Interaction): The discord that triggered the error
            error (app_commands.AppCommandError): Checks for unexpected error.

        Returns:
            None
        """
        embed_error_message = discord.Embed(
            title="Uh, oh! Something went wrong :(.",
            description=("An unexpected error occurred. Please open a ticket.",),
            # 0xE74C3C is Alizarin
            colour=0xE74C3C,
        )

        await error_message(interaction, embed=embed_error_message)
        logger.error(f"Unexpected error: {error}")


bot = OutBot(
    command_prefix=None,
    intents=discord.Intents.default(),
)


try:
    bot.run(DISCORD_TOKEN)


except TypeError:
    raise RuntimeError(
        'Invalid bot token. Please enter your discord bot token in a file called ".env" (you have to create it yourself) inside the folder "config".',
    )


except discord.LoginFailure:
    raise RuntimeError(
        'Invalid bot token. Please enter your discord bot token in a file called ".env" (you have to create it yourself) inside the folder "config".',
    )

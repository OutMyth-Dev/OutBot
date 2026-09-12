import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from config import custom_logger

custom_logger()
logger = logging.getLogger(__name__)


load_dotenv("config/.env")
DISCORD_TOKEN: str | None = os.getenv("DISCORD_TOKEN")
if DISCORD_TOKEN is None:
    raise RuntimeError("Your discord token cannot be none.")


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

        self.tree.on_error = self.on_app_command_error
        await self.tree.sync()

    async def on_app_command_error(
        self,
        interaction: discord.Interaction,
        error: discord.app_commands.AppCommandError,
    ) -> None:
        """
        Sends an embed when unexpected errors occur or tells when they can use a commands again. (30 second cooldown.)

        Args:
            interaction (discord.Interaction): The discord that triggered the error
            error (app_commands.AppCommandError): Checks errors.

        Returns:
            None
        """
        command_cooldown_error = isinstance(
            error, discord.app_commands.CommandOnCooldown
        )
        text = f"Rate limited! Try again in {error.retry_after:.2f} seconds."
        if interaction.response.is_done():
            await interaction.followup.send_message(
                text,
                ephemeral=True,
            )
            return
        else:
            await interaction.response.send_message(
                text,
                ephemeral=True,
            )
            return


        embed_error_message = discord.Embed(
            title="Something went wrong :(",
            description="An unexpected error occurred. Please open a ticket. This is may be an with OutBot's code or discord.",
            colour=discord.Colour.dark_red(),
        )
        if interaction.response.is_done():
            await interaction.followup.send(
                embed=embed_error_message,
                ephemeral=True,
            )

        else:
            await interaction.response.send_message(
                embed=embed_error_message,
                ephemeral=True,
            )
        logger.error(f"Unexpected error: {error}")


bot = OutBot(
    command_prefix="\0",
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

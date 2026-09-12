import discord
from discord import app_commands
from discord.ext import commands

from config import (
    GITHUB_LINK,
    PRIVACY_POLICY,
    RETENTION,
)


class PrivacyCommands(commands.Cog):
    """
    Information about privacy (OutBot).

    Attributes:
        None

    Methods:
        privacy: Information about OutBot's privacy.
        data: What data does Outbot collect about you?
        logs: What does OutBot log?
    """

    @discord.app_commands.command(
        name="privacy",
        description="Privacy related information about OutBot.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def privacy(self, interaction: discord.Interaction) -> None:
        """
        Privacy related information about OutBot

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message = discord.Embed(
            title="🔒 Information About OutBot's Privacy\n\n",
            description=(
                "- Logs: Only used to debug and are stored locally.\n"
                f"- Log Retention: {RETENTION}\n"
                f"- Source: Open source ({GITHUB_LINK})\n"
                f"- {PRIVACY_POLICY}\n"
            ),
            colour=discord.Colour.dark_blue(),
        )
        embed_message.set_footer(text=f"OutBot is Open source: {GITHUB_LINK}")

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="data",
        description="Information on what data OutBot retains.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def data(self, interaction: discord.Interaction) -> None:
        """
        What data does OutBot collect about you/process

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message = discord.Embed(
            title="🗃️ What data does OutBot keep about you and what does it log?\n\n",
            description=(
                "Data: Errors only.\n"
                "e.g. HTTPException: Only what command the error occurred in and the error is logged.\n"
                "Some data | (log level) ERROR | (file name) __main__ | Unexpected error: Command 'command name' raised an exception: some exception."
            ),
            colour=discord.Colour.dark_embed(),
        )
        embed_message.set_footer(text="OutBot does NOT collect any user data.")

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="logs",
        description="Information about OutBot's logs.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def logs(self, interaction: discord.Interaction) -> None:
        """
        What does OutBot log?

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message = discord.Embed(
            title="Information about what OutBot logs.\n\n",
            description=(
                f"OutBot retains logs for {RETENTION}.\n"
                "OutBot uses mode a to log (logger opens the file and appends to it).\n"
                "OutBot does **NOT** log any user data.\n"
                "OutBot only logs errors and logs are only used to make debugging easier.\n"
                f"OutBot is **open source. You can always check** out its source code/README for more information: {GITHUB_LINK}\n"
                "# This is what OutBot's logs actually looks like. These are 50 lines taken from OutBot's actual logs, sanitized and eaiser for non-programmers to read. Repeated logs were removed for readability.\n"
                "Time | Log Level | Name | message\n"
                "Time | Log Level | Name | message\n"
                "More (Time | Log Level | Name | message)"
                "Traceback Some Traceback\n"
                "AttributeError: 'something' object has no attribute 'something else'\n"
            ),
            colour=discord.Colour.green(),
        )

        await interaction.response.send_message(embed=embed_message)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PrivacyCommands(bot))

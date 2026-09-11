import discord
from discord import app_commands
from discord.ext import commands

from config import (
    DISCORD_SERVER_INVITE_LINK,
    OUTBOT_INVITE_LINK,
    OUTMYTH_YOUTUBE_CHANNEL_LINK,
)


class LinksCommands(commands.Cog):
    """
    Useful links about OutBot/OutMyth.

    Attributes:
        None

    Methods:
        youtube: Sends OutMyth's YouTube channel link.
        discord: Sends OutMyth's Discord server link.
        invite: Sends the invite link for OutBot.
    """

    @discord.app_commands.command(
        name="youtube",
        description="OutMyth's YouTube channel link",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def youtube(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends the OutMyth's YouTube channel link

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(f"{OUTMYTH_YOUTUBE_CHANNEL_LINK}")

    @discord.app_commands.command(
        name="discord",
        description="OutMyth's Discord server invite link.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def outmyth_discord_server_invite_link(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutMyth's Discord server invite link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        await interaction.response.send_message(f"{DISCORD_SERVER_INVITE_LINK}")

    @discord.app_commands.command(
        name="invite",
        description="OutBot's invite link.",
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def invite(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends OutBot invite link to allow users to invite OutBot to their server's.

        Args:
            interaction (discord.Interaction): The Discord command being invoked

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(f"{OUTBOT_INVITE_LINK}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LinksCommands(bot))

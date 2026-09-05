import discord
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

    Methords:
        youtube: Sends OutMyth's YouTube channel link.
        serverlink: Sends OutMyth's Discord server link.
        invite: Sends the invite link for OutBot.
    """

    @discord.app_commands.command(
        name="youtube",
        description="OutMyth's YouTube channel link",
    )
    async def youtube(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends the OutMyth's YouTube channel link

        Args:
            interactin (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        await interaction.response.send_message(
            f"# OutMyth's YouTube Channel:\n\n{OUTMYTH_YOUTUBE_CHANNEL_LINK}"
        )

    @discord.app_commands.command(
        name="discord",
        description="OutMyth's Discord server invite link.",
    )
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
        await interaction.response.send_message(
            f"# OutMyth's Discord Server:\n\n{DISCORD_SERVER_INVITE_LINK}"
        )

    @discord.app_commands.command(
        name="invite",
        description="OutBot's invite link.",
    )
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
        """
        await interaction.response.send_message(
            f"# Outbot's Invite Link:\n\n{OUTBOT_INVITE_LINK}"
        )


async def setup(bot: OutBot) -> None:
    await bot.add_cog(LinksCommands(bot))

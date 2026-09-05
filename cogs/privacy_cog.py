import discord
from discord.ext import commands

from config import (
    GITHUB_LINK,
    OUTBOT_LICENSE,
    PRIVACY_POLICY,
    RETENTION,
)


class PrivacyCommands(commands.Cog):
    """
    Infomration about privacy (OutBot).

    Attributes:
        None

    Methords:
        privacy: Infomraton about OutBot's privacy.
        data: What data does Outbot collect about you?
        logs: What does OutBot log?
    """

    @discord.app_commands.command(
        name="privacy",
        description="Privacy related information about OutBot.",
    )
    async def privacy(self, interaction: discord.Interaction) -> None:
        """
        Privacy related information about OutBot

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        embed_message = discord.Embed(
            title="🔒 OutBot Privacy\n\n",
            description=(
                "- Logs: Only used to degug and are stored locally.\n"
                f"- Retention: {RETENTION}\n"
                f"- Source: Open source ({GITHUB_LINK})\n"
                f"- Privacy Policy: {PRIVACY_POLICY}\n"
            ),
            # 0x00008B is Dark Blue
            colour=0x00008B,
        )
        embed_message.set_footer(text=f"OutBot is Open source: {GITHUB_LINK}")

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="data",
        description="Information on what data OutBot retains.",
    )
    async def data(self, interaction: discord.Interaction) -> None:
        """
        What data does OutBot collect about you/process

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        embed_message = discord.Embed(
            title="🗃️ What data does OutBot keep about you and what does it log?\n\n",
            description=(
                "Data: When an exception catches an error.\n"
                "eg: HTTPException. Only what the error was is logger.\n"
            ),
            # 0x2ECC71 is Emerald Green
            colour=0x2ECC71,
        )
        embed_message.set_footer(text="OutBot does NOT collect any user data.")

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="logs",
        description="Information about OutBot's logs.",
    )
    async def retention(self, interaction: discord.Interaction) -> None:
        """
        What does Outbot log?

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        embed_message = discord.Embed(
            title="Information about what OutBot logs.\n\n",
            description=(
                f"OutBot retains logs for {RETENTION}.\n"
                "OutBot uses mode a to log (logger opens the file and appends to it).\n"
                "OutBot does **NOT** log any user data.\n"
                f"OutBot is **open source. You can always check** out its source code/README for more information: {GITHUB_LINK}\n"
            ),
            # Turquoiseis 0x1ABC9
            colour=0x1ABC9,
        )

        await interaction.response.send_message(embed=embed_message)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(PrivacyCommands(bot))

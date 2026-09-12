import discord
from discord import app_commands
from discord.ext import commands

from config import DEVELOPER, DISCORD_SERVER_INVITE_LINK, GITHUB_LINK


class DeveloperCommands(commands.Cog):
    """
    Information about OutBot's developers.

    Attributes:
        None

    Methods:
        developers: Sends an embed of OutBot's developer's, with a link to where other developers can apply.
    """

    @discord.app_commands.command(
        name="developers", description="What developers contributed to OutBot?"
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def developers(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends the developers that develop OutBot.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        embed_message = discord.Embed(
            title="OutBot's Developers",
            description=f"{DEVELOPER} is the only developer for OutBot currently.",
            colour=discord.Colour.red(),
        )
        embed_message.set_footer(
            text=f"You can apply here: {DISCORD_SERVER_INVITE_LINK}"
        )
        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(name="gihub", description="OutBot's GitHub")
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def github(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends Outbot's GitHub link.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(f"{GITHUB_LINK}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DeveloperCommands(bot))

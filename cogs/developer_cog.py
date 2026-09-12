import discord
from discord import app_commands
from discord.ext import commands

from config import DEVELOPER, DEVELOPER_ID, DISCORD_SERVER_INVITE_LINK, GITHUB_LINK


class DeveloperCommands(commands.Cog):
    """
    Information about OutBot's developers.

    Attributes:
        None

    Methods:
        developers: Sends an embed of OutBot's developer's, with a link to where other developers can apply.
    """

    def __init__(self, bot):
        self.bot = bot

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

    @discord.app_commands.command(name="github", description="OutBot's GitHub")
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

    @discord.app_commands.command(
        name="sync", description="Sync Command Tree. (Only for developers)"
    )
    @app_commands.checks.cooldown(1, 86400, key=lambda interaction: interaction.user.id)
    async def sync(self, interaction: discord.Interaction) -> None:
        """
        Syncs Bot Command Tree

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None

        Cooldown:
            1 message per user every 86400 seconds or 1 message per user every day. This only applies the command they just used.
        """
        if interaction.user.id != DEVELOPER_ID:
            await interaction.response.send_message(
                "Hey! This command is only for developers!", ephemeral=True
            )
            return

        await self.bot.tree.sync()

        await interaction.response.defer()

        await interaction.followup.send(
            "Command tree synced!",
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DeveloperCommands(bot))

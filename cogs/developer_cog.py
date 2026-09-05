import discord
from discord.ext import commands

from config import DEVELOPERS, DISCORD_SERVER_INVITE_LINK


class DeveloperCommands(commands.Cog):
    """
    Information about OutBot's devleopers.

    Attributes:
        None

    Methords:
        developers: Sends an embed of OutBot's developer's, with a link to where other developers can apply.
    """

    @discord.app_commands.command(
        name="developers", description="What developers contributed to OutBot?"
    )
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
        """
        embed_message = discord.Embed(
            title="OutBot's Developers",
            description=f"{DEVELOPERS} is the only developer for OutBot currently.",
            # 0xFF0000 is Red
            colour=0xFF0000,
        )
        embed_message.set_footer(
            text=f"You can apply here: {DISCORD_SERVER_INVITE_LINK}"
        )
        await interaction.response.send_message(embed=embed_message)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(DeveloperCommands(bot))

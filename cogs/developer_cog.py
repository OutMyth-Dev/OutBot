import discord
from discord.ext import commands

from config import DISCORD_SERVER_INVITE_LINK


class DeveloperCommands(commands.Cog):
    @discord.app_commands.command(
        name="developers", description="What developers contributed to OutBot?"
    )
    async def developers(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends the developers for OutBot.

        Args:
            interaction: The discord command being invoked.
        
        Returns:
            None
        """
        embed_message = discord.Embed(
            title="OutBot's Developers",
            description="Mythoridan is the only developer for OutBot currently.",
            colour=0xE74C3C,
        )
        embed_message.set_footer(
            text=f"You can apply here: {DISCORD_SERVER_INVITE_LINK}"
        )
        await interaction.response.send_message(embed=embed_message)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(DeveloperCommands(bot))

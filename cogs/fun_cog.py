import discord
from discord.ext import commands

from config import CENSOR_WORDS
from utils import send_censor_word_warning


class FunCommands(commands.Cog):
    @discord.app_commands.command(
        name="freenitro",
        description="Free nitro!!!!",
    )
    async def rickroll(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """Sends a gif to rickroll the user."""

        await interaction.response.send_message(
            "https://tenor.com/view/rick-roll-nitro-gif-21997352",
            ephemeral=True,
        )

    @discord.app_commands.command(name="fakeban", description="Fake bans a user.")
    @discord.app_commands.describe(
        user="Who do you want to ban?",
        reason="Why would you like to ban them?",
        duration="How long will you like to ban this user for?",
        delete_messages="How many of the user's messages would you like to delete?",
    )
    async def fakeban(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
        reason: str,
        duration: int,
        delete_messages: int,
    ) -> None:
        if await send_censor_word_warning(interaction, reason):
            return

        embed_message = discord.Embed(
            title=f"{user} has been banned",
            description=reason,
            colour=0xFF0000,
        )
        embed_message.set_footer(text="Wait, why are they still here?")

        await interaction.response.send_message(embed=embed_message)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(FunCommands(bot))

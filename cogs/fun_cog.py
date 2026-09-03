import discord
from discord.ext import commands

from utils import send_censor_word_warning


class FreeNitroButton(discord.ui.View):
    @discord.ui.button(
        label="Click me for free nitro!!!",
        style=discord.ButtonStyle.success,
    )
    async def free_nitro_button_callback(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button,
    ) -> None:
        await interaction.response.send_message(
            "https://tenor.com/view/rick-roll-nitro-gif-21997352",
            ephemeral=True,
        )


class FunCommands(commands.Cog):
    @discord.app_commands.command(
        name="freenitro",
        description="Free nitro!",
    )
    async def rickroll(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        Sends a gif to rickroll the user.

        Args:
            interaction: The discord commmand being invoked
        
        Returns:
            None
        """

        await interaction.response.send_message(view=FreeNitroButton())
        await interaction.followup.send(
            "NEVER CLICK ON RANDOM BUTTONS THAT 'GUARANTEE' FREE STUFF ON THE INTERNET.",
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
        """
        Fake bans the user.

        Args:
            interaction: The discord command being invoked.
            user: Who does the the person using the command want to ban?
            reason: What is the reason for banning them?
            duration: How long do they want the user to stay banned.
            delete_messages: How many of their messages do they want to delete?
        Returns:
            None
        """
        if await send_censor_word_warning(interaction, reason):
            return

        embed_message = discord.Embed(
            title=f"{user} has been banned",
            description=reason,
            colour=0xFF0000,
        )
        embed_message.set_footer(text="Wait, how are they still here?")

        await interaction.response.send_message(embed=embed_message)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(FunCommands(bot))

import logging


import discord
from discord.ext import commands


from utils import send_error_message


logger = logging.getLogger(__name__)


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

        try:
            await interaction.response.send_message(
                "https://tenor.com/view/rick-roll-nitro-gif-21997352",
                ephemeral=True,
            )

        except discord.HTTPException:
            logger.exception("Discord's API failed when using /rickroll")

            await send_error_message(
                interaction, "Discord's API failed when using /rickroll."
            )

        except Exception:
            logger.exception("Unexpected error in /rickroll.")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="fakeban",
        description="Fake bans a user."
    )

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

        embed_message = discord.Embed(
            title=f"{user} has been banned",
            description=reason,
            colour=0xFF0000,
        )
        embed_message.set_footer(
            text="Wait, why are they still here?"
        )

        await interaction.response.send_message(embed=embed_message)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(FunCommands(bot))

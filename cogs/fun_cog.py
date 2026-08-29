import logging


import discord
from discord.ext import commands


from utils import send_error_message


logger = logging.getLogger(__name__)


class FunCommands(commands.Cog):

    
    @discord.app_commands.command(
        name="freenitro",
        description="Use this command to revieve a suprise...",
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


async def setup(bot: OutBot) -> None:
    await bot.add_cog(FunCommands(bot))

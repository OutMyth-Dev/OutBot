import logging

import discord
from discord.ext import commands

from utils import http_error, exception_error

logger = logging.getLogger(__name__)


class FunCommands(commands.Cog):
    @discord.app_commands.command(
        name="rickroll",
        description="Don't do it...",
    )
    async def rickroll(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """Sends the user a YouTube link to Rickroll them."""

        try:
            await interaction.response.send_message(
                "CLICK ME ---> ||<https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1>||",
                ephemeral=True,
            )

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /rickroll",
            )
            http_error(interaction, "Discord's API failed when using /rickroll.")

        except Exception:
            logger.exception("Unexpected error in /rickroll.")

            exception_error(
                interaction, "Something went wrong :(. Please open a ticket."
            )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(FunCommands(bot))

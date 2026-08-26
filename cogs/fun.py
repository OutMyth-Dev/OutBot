import logging

import discord
from discord.ext import commands

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

        logger.info(
            f"/rickroll was used by {interaction.user}",
        )

        try:
            await interaction.response.send_message(
                "CLICK ME ---> ||<https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1>||",
                ephemeral=True,
            )

        except discord.HTTPException:
            logger.exception(
                f"Discord's API failed when using /rickroll {interaction.user}"
            )
            await interaction.followup.send("Discord's API failed.")

        except Exception:
            logger.exception(f"Unexpected error in /rickroll {interaction.user}")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using /rickroll. Please open a ticket.",
                    ephemeral=True,
                )

            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using /rickroll. Please open a ticket.",
                    ephemeral=True,
                )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(FunCommands(bot))

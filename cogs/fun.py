import logging

import discord
from config.bot_info import RICKROLL_USER
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
            "/rickroll was used by %s",
            interaction.user,
        )

        try:
            await interaction.response.send_message(
                f"CLICK ME ---> ||{RICKROLL_USER}||",
                ephemeral=True,
            )

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /rickroll %s", interaction.user
            )
            await interaction.followup.send("Discord's API failed.")

        except Exception:
            logger.exception("Unexpected error in /rickroll%s", interaction.user)

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using /rickroll. "
                    "Please open a ticket.",
                    ephemeral=True,
                )

            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using /rickroll. Please open a ticket.",
                    ephemeral=True,
                )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(FunCommands(bot))

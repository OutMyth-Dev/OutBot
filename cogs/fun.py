import logging

import discord
from discord.ext import commands


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
            logging.exception("Discord's API failed when using /rickroll")
            await interaction.followup.send("Discord's API failed.")

        except Exception:
            logging.exception("Unexpected error in /rickroll")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using /rickroll. "
                    "Please open a ticket.",
                    ephemeral=True,
                )

            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using /rickroll. "
                    "Please open a ticket.",
                    ephemeral=True,
                )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(FunCommands(bot))

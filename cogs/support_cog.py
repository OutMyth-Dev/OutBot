import logging


import discord
from discord.ext import commands


logger = logging.getLogger(__name__)


class SupportCommands(commands.Cog):


    @discord.app_commands.command(
        name="reporthelp",
        description="Teaches you how to report."
    )
    async def reporthelp(
        self, 
        interaction: discord.Interaction
    ) -> None:
        try:
            await interaction.response.send_message(
                "# How do I report?\n\n"
                "You should Inculde:\n"
                "- Your discord username.\n"
                "- What your issue is.\n"
                "- Users username only if you're reporting a user.\n"
                "- Make sure you provide a lot of detail.\n"
                "- Please make sure you include a way for us to contact you.\n"
                "MAKE SURE YOUR REPORT IS UNDER 2000 CHARACTERS",
                ephemeral=True
            )
    
        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /reporthelp",
            )
            await http_error(
                interaction, "Discord's API failed when using /reporthelp."
            )

        except Exception:
            logger.exception("Unexpected error in /reporthelp.")

            await exception_error(
                interaction, "Something went wrong :(. Please open a ticket."
            )

    """This command will be implemented."""

    # @discord.app_commands.command(
    #     name="report",
    #     description="Report an issue/user. Please use /reporthelp; OutBot's README to know how to report.",
    # )
    # async def report(
    # self, 
    # interaction: discord.Interaction, report: str
    # ) -> None:
    #     reports.append(report)
    #     await interaction.response.send_message("Report has been sent", ephemeral=True)



async def setup(bot: OutBot) -> None:
    await bot.add_cog(SupportCommands(bot))
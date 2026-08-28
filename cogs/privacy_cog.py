import logging


import discord
from discord.ext import commands


from config import GITHUB_LINK ,OUTBOT_LICENSE, RETENTION
from utils import send_error_message


logger = logging.getLogger(__name__)


class PrivacyCommands(commands.Cog):


    @discord.app_commands.command(
        name="privacy",
        description="Privacy related information about OutBot."
    )
    async def privacy(self, interaction: discord.Interaction) -> None:   
        try:
            await interaction.response.send_message(
                "# 🔒 OutBot Privacy\n\n"
                "Logs: Only used to degug and are stored locally.\n"
                f"Retention: {RETENTION}\n"
                f"Source: Open source ({GITHUB_LINK})\n"
                f"OutBot's License: {OUTBOT_LICENSE}\n"
                "Privacy Policy: Coming Out Tommorow\n"
                "TOS: Coming Out Tommorow"
        )
        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /privacy",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /privacy."
            )
        except Exception:
            logger.exception("Unexpected error in /privacy")
            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )
            

    @discord.app_commands.command(
        name="data",
        description="Information on what data OutBot retains.",
    )
    async def data(
        self, 
        interaction: discord.Interaction
    ) -> None:
        try:
            await interaction.response.send_message(
            "# 🗃️ What data does OutBot keep **about you** and what does it log?\n\n"
            "Data: When an exception catches an error. eg: HTTPException. Only what the error was and what command the error occurred in is logged.\n"                  
            )
        except HTTPException:
            logger.exception(
                "Discord's API failed when using /data",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /data."
            )
        except Exception:
            logger.exception("Unexpected error in /data")
            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="logs",
        description="Information about OutBot's logs.",
    )
    async def retention(
        self, 
        interaction: discord.Interaction
    ) -> None:
        try:
            interaction.response.send_message(
                "# ⏳ How long does OutBot retain logs for?\n\n"
                f"OutBot retains logs for {RETENTION}.\n"
                "OutBot uses mode a to log (append).\n"
                "It does not log any user data.\n"
                f"# OutBot is open source. You can always check out its source code/README for me information. {GITHUB_LINK}"
            )
        except HTTPException:
            logger.exception(
                "Discord's API failed when using /logs",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /logs."
            )
        except Exception:
            logger.exception("Unexpected error in /logs")
            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


async def setup(bot: OutBot) -> None:
    await bot.add_cog(PrivacyCommands(bot))
    
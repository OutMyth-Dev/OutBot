import logging


import discord
from discord.ext import commands


from config import GITHUB_LINK ,OUTBOT_LICENSE, RETENTION
from utils import send_error_message


logger = logging.getLogger(__name__)


class PrivacyCommands(commands.Cog):


    @discord.app_commands.command(
        name="privacy",
        description="Privacy related information about OutBot.",
    )
    async def privacy(
        self, 
        interaction: discord.Interaction
    ) -> None:   
        try:
            
            embed_message = discord.Embed(
                title="🔒 OutBot Privacy\n\n",
                description=(
                    "- Logs: Only used to degug and are stored locally.\n"
                    f"- Retention: {RETENTION}\n"
                    f"- Source: Open source ({GITHUB_LINK})\n"
                    f"- OutBot's License: {OUTBOT_LICENSE}\n"
                    "- Privacy Policy: Coming Out Tommorow\n"
                    "- TOS: Coming Out Tommorow"),
                    colour=0x00008B,
                )
            embed_message.set_footer(
                text=f"OutBot is Open source {GITHUB_LINK}"
            )
            
            await interaction.response.send_message(embed=embed_message)

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
            embed_message = discord.Embed(
                title="🗃️ What data does OutBot keep **about you** and what does it log?\n\n"
                description=(
                    "Data: When an exception catches an error.\n" 
                    "eg: HTTPException. Only what the error was and what command the error occurred in is logged.\n",
                ),
                colour=0x2ECC71
            )
            embed_message.set_footer("OutBot does NOT collect any user data.")

            await interaction.response.send_message(embed=embed_message)

        except discord.HTTPException:
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
            embed_message = discord.Embed(
                title="⏳ How long does OutBot retain logs for?\n\n"
                description=(
                    f"OutBot retains logs for {RETENTION}.\n"
                    "OutBot uses mode a to log (logger opens the file and appends).\n"
                    "It does not log any user data.\n"
                    f"# OutBot is open source. You can always check out its source code/README for more information. {GITHUB_LINK}",
                ),
                colour=0x1ABC9
            )

            await interaction.response.send_message(embed=embed_message)

        except discord.HTTPException:
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
    
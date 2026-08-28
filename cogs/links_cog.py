import logging


import discord
from discord.ext import commands


from config import (
    DISCORD_SERVER_INVITE_LINK,
    OUTBOT_INVITE_LINK,
    OUTMYTH_YOUTUBE_CHANNEL_LINK,
)
from utils import send_error_message


logger = logging.getLogger(__name__)


class LinksCommands(commands.Cog):

    
    @discord.app_commands.command(
        name="youtube",
        description="OutMyth's YouTube channel link",
    )
    async def youtube(
        self,
        interaction: discord.Interaction,
    ) -> None:

        try:
            await interaction.response.send_message(
                f"# OutMyth's YouTube Channel:\n\n{OUTMYTH_YOUTUBE_CHANNEL_LINK}\n\n"
            )

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /youtube",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /youtube."
            )

        except Exception:
            logger.exception("Unexpected error in /youtube.")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="serverlink",
        description="OutMyth's Discord server invite link.",
    )
    async def serverlink(
        self,
        interaction: discord.Interaction,
    ) -> None:

        try:
            await interaction.response.send_message(
                f"# OutMyth's Discord Server:\n\n{DISCORD_SERVER_INVITE_LINK}"
            )

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /serverlink",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /serverlink."
            )

        except Exception:
            logger.exception("Unexpected error in /serverlink.")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="invite",
        description="Invite link for OutBot",
    )
    async def invite(
        self,
        interaction: discord.Interaction,
    ) -> None:

        try:
            await interaction.response.send_message(
                f"Outbot Invite Link:\n\n{OUTBOT_INVITE_LINK}"
            )

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /invite",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /invite."
            )

        except Exception:
            logger.exception("Unexpected error in /invite.")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


async def setup(bot: OutBot) -> None:
    await bot.add_cog(LinksCommands(bot))

import logging

import discord
from discord.ext import commands

from config.bot_info import OUTMYTH_YOUTUBE_CHANNEL_LINK, DISCORD_SERVER_INVITE_LINK, OUTBOT_INVITE_LINK
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
                "# OutMyth's YouTube Channel:\n\n"
                f"{OUTMYTH_YOUTUBE_CHANNEL_LINK}\n\n"
                f"{interaction.user.mention}"
            )
        except discord.HTTPException:
            logging.exception("Discord's API failed when using /youtube")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "Discord API failed when using /youtube.",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    "Discord API failed when using /youtube",
                    ephemeral=True,
                )

        except Exception:
            logging.exception("Unexpected error in /youtube")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using when using /youtube. "
                    "Please open a ticket.",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using when using /youtube. "
                    "Please open a ticket.",
                    ephemeral=True,
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
                "# OutMyth's Discord Server:\n\n"
                f"{DISCORD_SERVER_INVITE_LINK}\n\n"
                f"{interaction.user.mention}"
            )

        except discord.HTTPException:
            logging.exception("Discord's API failed when using /serverlink")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "Discord API failed when using /serverlink.",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    "Discord API failed when using /serverlink",
                    ephemeral=True,
                )

        except Exception:
            logging.exception("Unexpected error in /youtube")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using when using /serverlink. "
                    "Please open a ticket.",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using when using /serverlink. "
                    "Please open a ticket.",
                    ephemeral=True,
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
                "Outbot Invite Link:\n\n"
                f"{OUTBOT_INVITE_LINK}\n\n"
                f"{interaction.user.mention}"
            )

        except discord.HTTPException:
            logging.exception("Discord's API failed when using /invite")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "Discord API failed when using /invite.",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    "Discord API failed when using /invite",
                    ephemeral=True,
                )

        except Exception:
            logging.exception("Unexpected error in /youtube")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using when using /invite. "
                    "Please open a ticket.",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using when using /invite. "
                    "Please open a ticket.",
                    ephemeral=True,
                )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LinksCommands(bot))

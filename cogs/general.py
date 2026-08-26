import logging

import discord
from discord.ext import commands

from config.emojis import emojis
from config.max_chars import (
    MAX_MESSAGE_LENGTH,
    MAX_QUESTION_LENGTH,
    MAX_TITLE_AND_QUESTION_LENGTH,
    MAX_TITLE_LENGTH,
)

logger = logging.getLogger(__name__)


class GeneralCommands(commands.Cog):
    @discord.app_commands.command(
        name="hello",
        description="It pings you & says hello!",
    )
    async def hello(
        self,
        interaction: discord.Interaction,
    ) -> None:

        try:
            await interaction.response.send_message(
                "Hello, ",
                f"{interaction.user.mention}!",
            )

        except discord.HTTPException:
            logger.exception("Discord API failure when using /hello")
            await interaction.followup.send(
                "Discord API failure.",
                ephemeral=True,
            )

        except Exception:
            logger.exception("An unexpected error in /hello")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using /hello. Please open a ticket.",
                    ephemeral=True,
                )

            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using /hello. Please open a ticket.",
                    ephemeral=True,
                )

    @discord.app_commands.command(
        name="dm",
        description="DMs the user. Please make sure you have your DMs turned on.",
    )
    async def dm(
        self,
        interaction: discord.Interaction,
        msg: str,
    ) -> None:

        if len(msg) > MAX_MESSAGE_LENGTH:
            await interaction.response.send_message(
                f"Your message was too long.{MAX_MESSAGE_LENGTH}",
                ephemeral=True,
            )
            return

        try:
            await interaction.user.send(f"Secret Message: ||{msg}||")
            (
                await interaction.response.send_message(
                    "Check your DMs!",
                    ephemeral=True,
                ),
            )

        except discord.Forbidden:
            logger.exception("User had their DMs turned off.")
            await interaction.response.send_message(
                "I could not send you a DM. This is because you have them turned off.",
                ephemeral=True,
            )

        except discord.HTTPException:
            logger.exception("Discord API failure in /dm")
            await interaction.followup.send(
                "Discord's API failed.",
                ephemeral=True,
            )

        except Exception:
            logger.exception("Unexpected error in /dm")
            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using /dm. Please open a ticket.",
                    ephemeral=True,
                )

            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using /dm. Please open a ticket.",
                    ephemeral=True,
                )

    @discord.app_commands.command(
        name="say",
        description="You tell the OutBot what to say!",
    )
    async def say(
        self,
        interaction: discord.Interaction,
        say: str,
    ) -> None:

        if len(say) > MAX_MESSAGE_LENGTH:
            await interaction.response.send_message(
                f"Your message was too long.{MAX_MESSAGE_LENGTH}",
                ephemeral=True,
            )
            return

        try:
            await interaction.response.send_message(
                f"{interaction.user.mention} told me to say: ||{say}||"
            )

        except discord.HTTPException:
            logger.exception("Discord API failure in /say.")
            await interaction.followup.send(
                "Discord API failure",
                ephemeral=True,
            )

        except Exception:
            logger.exception("Unexpected error in /say")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using /say. Please open a ticket.",
                    ephemeral=True,
                )

            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using /say. Please open a ticket.",
                    ephemeral=True,
                )

    @discord.app_commands.command(
        name="ping",
        description="Pings you",
    )
    async def ping(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message(f"{interaction.user.mention}")

    @discord.app_commands.command(
        name="poll",
        description="Create a new poll.",
    )
    async def poll(
        self,
        interaction: discord.Interaction,
        title: str,
        question: str,
    ) -> None:
        """10 reactions to allow the user to pick a reaction of their choice or they can pick their own."""

        if len(title) > MAX_TITLE_LENGTH and len(question) > MAX_QUESTION_LENGTH:
            await interaction.response.send_message(
                f"Your title and length are too long. {MAX_TITLE_AND_QUESTION_LENGTH}",
                ephemeral=True,
            )
            return

        if len(title) > MAX_TITLE_LENGTH:
            await interaction.response.send_message(
                f"Your title is too long.{MAX_TITLE_LENGTH}",
                ephemeral=True,
            )
            return

        if len(question) > MAX_QUESTION_LENGTH:
            await interaction.response.send_message(
                f"Your question is too long.{MAX_QUESTION_LENGTH}",
                ephemeral=True,
            )
            return

        try:
            embed = discord.Embed(
                title=title,
                description=question,
            )

            await interaction.response.send_message(embed=embed)

            poll_msg = await interaction.original_response()

            try:
                for emoji in emojis:
                    await poll_msg.add_reaction(emoji)

            except discord.HTTPException:
                logger.exception("Discords API failure in /poll.")
                await interaction.followup.send(
                    "Poll created but failed adding emojis. Please open a ticket.",
                    ephemeral=True,
                )

        except discord.HTTPException:
            logger.exception("Discord's API failure in /poll")
            await interaction.followup.send(
                "Discord API failure.",
                ephemeral=True,
            )

        except Exception:
            logger.exception("Unexpected error in /poll")

            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using /poll. Please open a ticket.",
                    ephemeral=True,
                )
            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using /poll. Please open a ticket.",
                    ephemeral=True,
                )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GeneralCommands(bot))

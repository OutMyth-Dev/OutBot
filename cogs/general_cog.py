import logging


import discord
from discord.ext import commands


from config import MAX_MESSAGE_LENGTH, MAX_QUESTION_LENGTH, MAX_TITLE_LENGTH, emojis
from utils import send_error_message


logger = logging.getLogger(__name__)


class GeneralCommands(commands.Cog):

    
    @discord.app_commands.command(
        name="hello",
        description="It says hello!",
    )
    async def hello(
        self,
        interaction: discord.Interaction,
    ) -> None:

        try:
            await interaction.response.send_message(
                "Hello",
            )

        except discord.HTTPException:
            logger.exception("Discord's API failed when using /hello")

            await send_error_message(
                interaction, "Discord's API failed when using /hello."
            )

        except Exception:
            logger.exception("Unexpected error in /hello.")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="dm",
        description="DMs the user. Please make sure you have your DMs turned on.",
    )
    async def dm(
        self,
        interaction: discord.Interaction,
        message: str,
    ) -> None:

        if len(message) > MAX_MESSAGE_LENGTH:
            await interaction.response.send_message(
                f"Your message was too long. Please make it less than {MAX_MESSAGE_LENGTH} characters.",
                ephemeral=True,
            )
            return

        try:
            await interaction.user.send(f"Secret Message:  ||{message}||")
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
            logger.exception("Discord's API failed when using /dm")

            send_error_message(interaction, "Discord's API failed when using /dm.")

        except Exception:
            logger.exception("Unexpected error in /dm.")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="say",
        description="You tell the OutBot what to say!",
    )
    async def say(
        self,
        interaction: discord.Interaction,
        you_tell_me_what_to_say: str,
    ) -> None:

        if len(you_tell_me_what_to_say) > MAX_MESSAGE_LENGTH:
            await interaction.response.send_message(
                f"Your message was too long. Please make it less than {MAX_MESSAGE_LENGTH} characters.",
                ephemeral=True,
            )
            return

        try:
            embed()
            
            await interaction.response.send_message(
                f"{interaction.user.mention} Told me to say: ||{you_tell_me_what_to_say}||"
            )

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /say",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /say."
            )

        except Exception:
            logger.exception("Unexpected error in /say.")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="ping",
        description="Pings you",
    )
    async def ping(self, interaction: discord.Interaction) -> None:
        try:
            await interaction.response.send_message(f"{interaction.user.mention}")

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /ping",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /ping."
            )

        except Exception:
            logger.exception("Unexpected error in /ping")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="poll",
        description="Create a poll.",
    )
    @discord.app_commands.describe(
        title="What is your poll's title?",
        question="What is the question you would like to ask?"
    )
    async def poll(
        self,
        interaction: discord.Interaction,
        title: str,
        question: str,
    ) -> None:

        if len(title) > MAX_TITLE_LENGTH and len(question) > MAX_QUESTION_LENGTH:
            await interaction.response.send_message(
                f"Your title and length are too long. Please make your title under {MAX_TITLE_LENGTH} characters and your question under {MAX_QUESTION_LENGTH} characters.",
                ephemeral=True,
            )
            return

        if len(title) > MAX_TITLE_LENGTH:
            await interaction.response.send_message(
                f"Your title is too long. Please make it less than {MAX_TITLE_LENGTH} characters.",
                ephemeral=True,
            )
            return

        if len(question) > MAX_QUESTION_LENGTH:
            await interaction.response.send_message(
                f"Your question is too long. Please make it less than {MAX_QUESTION_LENGTH} characters.",
                ephemeral=True,
            )
            return

        try:
            embed_message = discord.Embed(
                title=title,
                description=question,
            )

            await interaction.response.send_message(embed=embed_message)

            poll_message = await interaction.original_response()

            try:
                for emoji in emojis:
                    await poll_message.add_reaction(emoji)

            except discord.HTTPException:
                logger.exception(
                    "Discord's API failed when using /poll",
                )
                await send_error_message(
                    interaction, "Poll created, but failed to add reactions. "
                )

        except discord.HTTPException:
            await logger.exception(
                "Discord's API failed when using /poll",
            )
            send_error_message(interaction, "Discord's API failed when using /poll.")

        except Exception:
            logger.exception("Unexpected error in /poll")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


async def setup(bot: OutBot) -> None:
    await bot.add_cog(GeneralCommands(bot))

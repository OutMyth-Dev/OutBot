import discord
from discord.ext import commands

from config import EMOJIS, MAX_MESSAGE_LENGTH, MAX_QUESTION_LENGTH, MAX_TITLE_LENGTH
from utils import send_censor_word_warning


class PingUserButton(discord.ui.View):
    @discord.ui.button(label="Ping Yourself!", style=discord.ButtonStyle.secondary)
    async def ping_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        await interaction.response.send_message(
            f"{interaction.user.mention}",
            ephemeral=True,
        )


class GeneralCommands(commands.Cog):
    @discord.app_commands.command(
        name="greet",
        description="OutBot greets you!",
    )
    async def greet(
        self,
        interaction: discord.Interaction,
    ) -> None:
        await interaction.response.send_message(
            f"Hello, {interaction.user.mention}! How are you?",
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
        if await send_censor_word_warning(interaction, message):
            return

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
            await interaction.response.send_message(
                "I could not send you a DM. This is because you have them turned off.",
                ephemeral=True,
            )

    @discord.app_commands.command(
        name="say",
        description="You tell the OutBot what to say!",
    )
    @discord.app_commands.describe(message="You tell OutBot what to say!")
    async def say(
        self,
        interaction: discord.Interaction,
        message: str,
    ) -> None:
        if await send_censor_word_warning(interaction, message):
            return

        if len(message) > MAX_MESSAGE_LENGTH:
            await interaction.response.send_message(
                f"Your message was too long. Please make it less than {MAX_MESSAGE_LENGTH} characters.",
                ephemeral=True,
            )
            return

        embed_message = discord.Embed(
            title=f"{interaction.user} has said: ",
            description=f"{message}",
            colour=0x2ECC71,
        )
        embed_message.set_footer(
            text="You may report the user if anything inappropiate was said."
        )
        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="ping",
        description="Click a magical button that pings you.",
    )
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(view=PingUserButton())

    @discord.app_commands.command(
        name="poll",
        description="Create a poll.",
    )
    @discord.app_commands.describe(
        title="What is your poll's title?",
        question="What is the question you would like to ask?",
    )
    async def poll(
        self,
        interaction: discord.Interaction,
        title: str,
        question: str,
    ) -> None:
        if await send_censor_word_warning(interaction, title or question):
            return

        if await send_censor_word_warning(interaction, title and question):
            return

        if len(title) > MAX_TITLE_LENGTH and len(question) > MAX_QUESTION_LENGTH:
            await interaction.response.send_message(
                f"Please make your title less than {MAX_TITLE_LENGTH} characters and your question less than {MAX_QUESTION_LENGTH} characters.",
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

        embed_message = discord.Embed(
            title=title,
            description=question,
        )

        await interaction.response.send_message(embed=embed_message)

        poll_message = await interaction.original_response()

        for emoji in EMOJIS:
            await poll_message.add_reaction(emoji)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(GeneralCommands(bot))

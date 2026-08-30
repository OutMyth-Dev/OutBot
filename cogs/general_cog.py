import discord
from discord.ext import commands

from config import MAX_MESSAGE_LENGTH, MAX_QUESTION_LENGTH, MAX_TITLE_LENGTH, emojis


class GeneralCommands(commands.Cog):
    @discord.app_commands.command(
        name="greet",
        description="It greets you!",
    )
    async def hello(
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

        if len(message) > MAX_MESSAGE_LENGTH:
            await interaction.response.send_message(
                f"Your message was too long. Please make it less than {MAX_MESSAGE_LENGTH} characters.",
                ephemeral=True,
            )
            return

        embed_message(
            title=f"{interaction.user.mention} has said: ",
            description=f"{message}",
            colour=0x2ECC71,
        )
        embed_message.set_footer(
            "You may report the user if something inappropiate was said."
        )
        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="ping",
        description="Pings you",
    )
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"{interaction.user.mention}")

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

        embed_message = discord.Embed(
            title=title,
            description=question,
        )

        await interaction.response.send_message(embed=embed_message)

        poll_message = await interaction.original_response()

        for emoji in emojis:
            await poll_message.add_reaction(emoji)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(GeneralCommands(bot))

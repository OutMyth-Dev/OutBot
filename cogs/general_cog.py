import discord
from discord.ext import commands

from config import EMOJIS, MAX_MESSAGE_LENGTH, MAX_QUESTION_LENGTH, MAX_TITLE_LENGTH
from utils import send_censor_word_warning


class PingUserButton(discord.ui.View):
    """
    Creates a button that is invoked when /ping is used.

    Attributes:
        None

    Methords:
        ping_button_callback: Sends a grey button which is invoked when /ping is used.
    """

    @discord.ui.button(label="Ping Yourself!", style=discord.ButtonStyle.secondary)
    async def ping_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.Button
    ) -> None:
        """
        Pings the user when the button is clicked.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Returns:
            None
        """
        await interaction.response.send_message(
            f"{interaction.user.mention}",
            ephemeral=True,
        )


class GeneralCommands(commands.Cog):
    """
    Commands that do not fit any other catagory.

    Attributes:
        None

    Methords:
        greet: Greets the user.
        dm: DMs the user.
        echo: OutBot says what the user passed in.
        ping: Pings the user when a button is pressed.
        poll: Creates a embed with a title, question, and 10 reactions.
    """

    @discord.app_commands.command(
        name="greet",
        description="OutBot greets you!",
    )
    async def greet(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot greets you.

        Args:
            interaction (discord.Interaction): The discord command being invoked.

        Returns:
            None
        """
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
        """
        DM the user who invoked the command.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            message (str): The message passed in by the user.

        Returns:
            None
        """
        if await send_censor_word_warning(interaction, message):
            return

        if len(message) > MAX_MESSAGE_LENGTH:
            await interaction.response.send_message(
                f"Your message was too long. Please make it less than {MAX_MESSAGE_LENGTH} characters.",
                ephemeral=True,
            )
            return

        try:
            await interaction.user.send(f"||{message}||")
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
        name="ehco",
        description="You tell the OutBot what to say!",
    )
    @discord.app_commands.describe(message="You tell OutBot what to say!")
    async def echo(
        self,
        interaction: discord.Interaction,
        message: str,
    ) -> None:
        """
        Says what the user passed in.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            message (str): The message the user wants to be said that is passed.

        Returns:
            None
        """
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
            # 0x2ECC71 is Emerald
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
        """
        Pings the user who invoked the command.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns None.
        """
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
        """
        Creates an embed with a title and a question that users can add reactions to.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            title (str): The title the user wants their embed to have.
            question (str): The question of their poll (description).

        Returns:
            None
        """
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

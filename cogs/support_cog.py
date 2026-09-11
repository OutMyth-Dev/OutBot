import discord
from discord import app_commands
from discord.ext import commands

from utils import send_censor_word_warning


class SupportCommands(commands.Cog):
    """
    Commands related to user support.

    Attributes:
        None

    Methods:
        reporthelp: Tells users what a good report should contain.
        report: The command users can use to report an issue.
        feedbackhelp: Tells users what good feedback should look like.
        feedback: The command users can use to give feedback.
    """

    @discord.app_commands.command(
        name="reporthelp", description="Explains what a good report looks like."
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def reporthelp(self, interaction: discord.Interaction) -> None:
        """
        Tells the user what makes a good report.

        Args:
            interaction (discord.Interaction): The command being invoked

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(
            "How do I make a good report?\n\n"
            "You should Include:\n"
            "- Your discord username.\n"
            "- What your issue is.\n"
            "- User's username only if you're reporting a user.\n"
            "- Make sure you provide as much detail as possible.\n"
            "- Please make sure you include a way for us to contact.\n"
            "- Your report/s are deleted as soon as they are dealt with.\n",
            ephemeral=True,
        )

    @discord.app_commands.command(
        name="report",
        description="Report an issue/user. Please use /reporthelp; OutBot's README to know how to report.",
    )
    @discord.app_commands.describe(
        report="Please describe what you would like to report. Use /reporhelp if you are unsure how to format a report."
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def report(
        self,
        interaction: discord.Interaction,
        report: app_commands.Range[str, 1, 1999],
    ) -> None:
        """
        A command users can use to report an issue.

        Args:
            interaction (discord.Interaction): The discord command being invoked
            report (str): What report the user passes in. Maximum length: 1999 characters.

        Allowed Mentions:
            N/A

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(interaction, report):
            return

        with open("reports.txt", "a") as reports:
            reports.write(report + "\n")

        await interaction.response.send_message("Report has been sent", ephemeral=True)

    @discord.app_commands.command(
        name="feedbackhelp", description="Explains what makes good feedback."
    )
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def feedbackhelp(self, interaction: discord.Interaction) -> None:
        """
        Tells users how to create good feedback

        Args:
            interaction (discord.Interaction): The discord command being invoked

        Returns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        await interaction.response.send_message(
            "How do I give OutBot's developers good feedback?\n\n"
            "You should Include:\n"
            "- What your feedback is.\n"
            "- Why you think it would make OutBot better.\n"
            "- Make sure you provide as much detail as possible.\n"
            "- Please make sure you include a way for us to contact.\n"
            "- Your feedback is deleted as soon as it is dealt with.\n"
            "- Your feedback can contain bug reporting and security reporting for now. You can also report a security issue using /report.\n",
            ephemeral=True,
        )

    @discord.app_commands.command(
        name="feedback",
        description="Provide OutBot useful feedback",
    )
    @discord.app_commands.describe(feedback="Give OutBot useful feedback.")
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def feedback(
        self,
        interaction: discord.Interaction,
        feedback: app_commands.Range[str, 1, 1999],
    ) -> None:
        """
        A command users can use to send feedback.

        Args:
            interaction(discord.Interaction): The discord command being invoked.
            feedback (str): What feedback the user passes in. Maximum length: 1999 characters.

        Allowed Mentions:
            N/A

        Retturns:
            None

        Cooldown:
            1 message per user every 30 seconds. This only applies the command they just used.
        """
        if await send_censor_word_warning(interaction, feedback):
            return

        with open("feedback.txt", "a") as user_feedback:
            user_feedback.write(feedback + "\n")

        await interaction.response.send_message(
            "Feedback has been sent!", ephemeral=True
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SupportCommands(bot))

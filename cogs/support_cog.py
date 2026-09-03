import discord
from discord.ext import commands

from config import MAX_FEEFBACK_LENGTH, MAX_REPORT_LENGTH
from utils import send_censor_word_warning


class SupportCommands(commands.Cog):
    """
    Commands related to user support.

    Attributes:
        None

    Methords:
        reporthelp: Tells users what a good report should contain.
        report: The command users can use to report an issue.
        feedbackhelp: Tells users what good feedback should look like.
        feedback: The command users can use to give feedback.
    """

    @discord.app_commands.command(
        name="reporthelp", description="Explains what a good report looks like."
    )
    async def reporthelp(self, interaction: discord.Interaction) -> None:
        """
        Tells the user what makes a good report.

        Args:
            interaction (discord.Interaction): The command being invoked

        Returns:
            None
        """
        await interaction.response.send_message(
            "How do I make a good report?\n\n"
            "You should Inculde:\n"
            "- Your discord username.\n"
            "- What your issue is.\n"
            "- User's username only if you're reporting a user.\n"
            "- Make sure you provide as much detail as possible.\n"
            "- Please make sure you include a way for us to contact.\n"
            f"MAKE SURE YOUR REPORT IS UNDER {MAX_REPORT_LENGTH} CHARACTERS.",
            ephemeral=True,
        )

    @discord.app_commands.command(
        name="report",
        description="Report an issue/user. Please use /reporthelp; OutBot's README to know how to report.",
    )
    @discord.app_commands.describe(
        report="Please describe what you would like to report. Use /reporhelp if you are unsure how to format a report."
    )
    async def report(
        self,
        interaction: discord.Interaction,
        report: str,
    ) -> None:
        """
        A command users can use to report an issue.

        Args:
            interaction (discord.Interaction): The discord command being invoked
            report (str): What report the user passes in.

        Returns:
            None
        """
        with open("reports.txt", "a") as report:
            report.write(report + "\n")

        if await send_censor_word_warning(interaction, report):
            return

        if len(report) > MAX_REPORT_LENGTH:
            await interaction.response.send_message(
                "Please make your report under 1999 character, or split it across multiple reports.",
                ephemeral=True,
            )
        await interaction.response.send_message("Report has been sent", ephemeral=True)

    @discord.app_commands.command(
        name="feedbackhelp", description="Explains what makes good feedback."
    )
    async def feedbackhelp(self, interaction: discord.Interaction) -> None:
        """
        Tells users how to create good feedback

        Args:
            interaction (discord.Interaction): The discord command being invoked

        Returns:
            None
        """
        await interaction.response.send_message(
            "How do I give OutBot's developers good feeback?\n\n"
            "You should Inculde:\n"
            "- What your feedback is.\n"
            "- Why you think it would make OutBot better.\n"
            "- Make sure you provide as much detail as possible.\n"
            "- Please make sure you include a way for us to contact.\n"
            "- Your feedback can contian bug reporting and security reporting for now. You can also report a security issue using /report."
            f"MAKE SURE YOUR FEEDBACK IS UNDER {MAX_FEEFBACK_LENGTH} CHARACTERS",
            ephemeral=True,
        )

    @discord.app_commands.command(
        name="feedback",
        description="Provide OutBot useful feedback",
    )
    @discord.app_commands.describe(
        feedback=f"Give OutBot useful feedback. Please make sure it is under {MAX_FEEFBACK_LENGTH} characters."
    )
    async def feedback(self, interaction: discord.Interaction, feedback: str) -> None:
        """
        A commmand users can use to send feedback.

        Args:
            interaction(discord.Interaction): The discord command being invoked.
            feedback (str): What feedback the user passes in.
        """
        with open("feedback.txt", "a") as feedback:
            feedback.write(feedback + "\n")

        if await send_censor_word_warning(interaction, feedback):
            return

        if len(feedback) > MAX_FEEFBACK_LENGTH:
            await interaction.response.send_message(
                "Please make your feedback under 1999 character, or split it across multiple feeback messages.",
                ephemeral=True,
            )
            return
        await interaction.response.send_message(
            "Feedback has been sent!", ephemeral=True
        )


async def setup(bot: OutBot) -> None:
    await bot.add_cog(SupportCommands(bot))

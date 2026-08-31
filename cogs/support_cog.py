import discord
from discord.ext import commands


from config import MAX_REPORT_LENGTH, MAX_FEEFBACK_LENGTH


class SupportCommands(commands.Cog):
    @discord.app_commands.command(
        name="reporthelp", description="Teaches you how to report."
    )
    async def reporthelp(self, interaction: discord.Interaction) -> None:

        await interaction.response.send_message(
            "How do I report?\n\n"
            "You should Inculde:\n"
            "- Your discord username.\n"
            "- What your issue is.\n"
            "- Users username only if you're reporting a user.\n"
            "- Make sure you provide a lot of detail.\n"
            "- Please make sure you include a way for us to contact you.\n"
            "MAKE SURE YOUR REPORT IS UNDER  CHARACTERS",
            ephemeral=True,
        )

    """This command will be implemented later. (Towords the end of update 0.5)"""

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

        with open("reports.txt", "a") as file:
            file.write(report + "\n")

        if len(report) > MAX_REPORT_LENGTH:
            await interaction.response.send_message(
                "Please make your report under 1999 character, or split it across multiple reports.",
                ephemeral=True,
            )
        await interaction.response.send_message(
            "Report has been sent", ephemeral=True
        )
        return

    @discord.app_commands.command(
        name="feedback",
        description="Provide OutBot useful feedback",
    )
    @discord.app_commands.describe(
        feedback=f"Give OutBot useful feedback. Please make sure it is under {MAX_FEEFBACK_LENGTH} characters."
    )
    async def feedback(
        self,
        interaction: discord.Interaction,
        feedback: str,
    ) -> None:

        with open("feedback.txt", "a") as file:
            file.write(feedback + "\n")

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

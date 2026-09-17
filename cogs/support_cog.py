import discord
from discord import app_commands
from discord.ext import commands

from utils import send_censor_word_warning


class ReportButton(discord.ui.View):
    """Creates a button that triggers when the /report command is invoked. This button asks if the user would like to proceed with their report."""

    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.button(
        label="Proceed?",
        emoji="➡️",
        style=discord.ButtonStyle.success,
    )
    async def report_proceed_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.button
    ) -> None:
        """
        Proceed with report.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            5 minute (300 seconds)
        """
        embed_message = discord.Embed(
            title="Report", description="Who would you like to report?"
        )
        embed_message.add_field(
            name="You are reporting", value=f"{interaction.user}", inline=True
        )
        embed_message.set_footer(text="Some steps remaining...")
        await interaction.response.send_message(embed=embed_message, ephemeral=True)

    @discord.ui.button(
        label="Cancel?",
        emoji="✖️",
        style=discord.ButtonStyle.danger,
    )
    async def report_cancel_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.button
    ) -> None:
        """
        Cancel the report.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            5 minute (300 seconds)
        """
        embed_message = discord.Embed(
            title="Cancelled", description="Your report has been cancelled."
        )
        embed_message.set_footer(text="Report cancelled at step 1.")
        await interaction.response.send_message(embed=embed_message, ephemeral=True)

    @discord.ui.button(
        label="Help?",
        emoji="🤝",
        style=discord.ButtonStyle.primary,
    )
    async def help_cancel_button_callback(
        self, interaction: discord.Interaction, button: discord.ui.button
    ) -> None:
        """
        Cancel the report.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.
            button (discord.ui.button): The button being created.

        Timeout:
            5 minute (300 seconds)
        """
        embed_message = discord.Embed(
            title="Help", description="Some help"
        )
        embed_message.set_footer(text="SOme help")
        await interaction.response.send_message(embed=embed_message, ephemeral=True)


class SupportCommands(commands.GroupCog, group_name="support"):
    """Commands related to user support."""

    @discord.app_commands.command(
        name="report",
        description="Report an issue/user.",
    )
    @discord.app_commands.describe(user="Who is the user who did this?")
    @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    async def report(
        self,
        interaction: discord.Interaction,
        user: discord.Member,
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
        # if await send_censor_word_warning(interaction):
        #     return

        await interaction.response.send_message(view=ReportButton())

    # @discord.app_commands.command(
    #     name="feedback",
    #     description="Provide useful feedback to OutBot.",
    # )
    # @discord.app_commands.describe(feedback="Give OutBot useful feedback.")
    # @app_commands.checks.cooldown(1, 30, key=lambda interaction: interaction.user.id)
    # async def feedback(
    #     self,
    #     interaction: discord.Interaction,
    #     feedback: app_commands.Range[str, 1, 1999],
    # ) -> None:
    #     """
    #     A command users can use to send feedback.

    #     Args:
    #         interaction(discord.Interaction): The discord command being invoked.
    #         feedback (str): What feedback the user passes in. Maximum length: 1999 characters.

    #     Allowed Mentions:
    #         N/A

    #     Returns:
    #         None

    #     Cooldown:
    #         1 message per user every 30 seconds. This only applies the command they just used.
    #     """
    #     if await send_censor_word_warning(interaction, feedback):
    #         return

    #     await interaction.response.send_message(
    #         "Feedback has been sent!", ephemeral=True
    #     )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SupportCommands(bot))

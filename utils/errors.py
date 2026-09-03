import discord


async def error_message(interaction: discord.Interaction, message: str) -> None:
    """
    Checks if the command has been responded to.

    Args:
        interaction (discord.Interaction): The Discord command that triggered an error.
        message (str): The error message the is going to be sent to the user.

    Returns:
        None
    """
    if interaction.response.is_done():
        await interaction.followup.send(
            message,
            ephemeral=True,
        )

    else:
        await interaction.response.send_message(
            message,
            ephemeral=True,
        )

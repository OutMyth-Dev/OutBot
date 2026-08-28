import discord


async def http_error(
    interaction: discord.Interaction,
    message: str,
) -> None:

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


async def exception_error(
    interaction: discord.Interaction,
    message: str,
) -> None:

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

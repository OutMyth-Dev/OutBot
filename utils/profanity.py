import discord

from config import CENSOR_WORDS


async def send_censor_word_warning(
    interaction: discord.Interaction, user_input: str
) -> bool:
    if any(word in user_input.lower() for word in CENSOR_WORDS):
        await interaction.response.send_message(
            "Your message cannot contain swear words.", ephemeral=True
        )
        return True
    return False

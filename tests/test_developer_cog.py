import pytest
from unittest.mock import AsyncMock, MagicMock

from cogs import DeveloperCommands
from config import DEVELOPER, DISCORD_SERVER_INVITE_LINK

@pytest.mark.asyncio
async def test_developer():
    developer_cog = DeveloperCommands(MagicMock())

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    await developer_cog.developers.callback(developer_cog, interaction)

    interaction.response.send_message(
        title="OutBot's Developers",
        description=f"{DEVELOPER} is the only developer for OutBot currently.",
        # 0xFF0000 is Red
        colour=0xFF0000,
    )
    interaction.response.send_message.set_footer(
        text=f"You can apply here: {DISCORD_SERVER_INVITE_LINK}"
    )
    
if __name__ == "__main__":
    test_developer()
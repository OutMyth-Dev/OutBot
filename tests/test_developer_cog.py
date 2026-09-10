from unittest.mock import AsyncMock, MagicMock

import pytest

from cogs import DeveloperCommands
from config import DEVELOPER, DISCORD_SERVER_INVITE_LINK


@pytest.mark.asyncio
async def test_developer() -> None:
    """
    This tests the command /developer.

    Args:
        None

    Returns:
        None
    """
    developer_cog = DeveloperCommands(MagicMock())

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    await developer_cog.developers.callback(developer_cog, interaction)

    interaction.response.send_message.assert_awaited_once()

    embed_message = interaction.response.send_message.await_args.kwargs["embed"]

    assert embed_message.title == "OutBot's Developers"
    assert (
        embed_message.description
        == f"{DEVELOPER} is the only developer for OutBot currently."
    )
    # 0xFF0000 is Red
    assert embed_message.colour.value == 0xFF0000
    assert (
        embed_message.footer.text == f"You can apply here: {DISCORD_SERVER_INVITE_LINK}"
    )


if __name__ == "__main__":
    test_developer()

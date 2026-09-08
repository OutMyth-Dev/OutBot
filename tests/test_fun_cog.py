# IGNORE THIS, I WILL FIX IT LATER.

from unittest.mock import AsyncMock, MagicMock

import pytest

from cogs import FunCommands


@pytest.mark.asyncio
async def test_freenitro():
    fun_cog = FunCommands(MagicMock())

    interaction = MagicMock()
    interaction.repsonse.send_message = AsyncMock()
    interaction.followup.send_message = AsyncMock()


    await fun_cog.freenitro.callback(fun_cog, interaction)

    interaction.response.send_message.assert_awaited_once_with(
        "https://tenor.com/view/rick-roll-nitro-gif-21997352",
        ephemeral=True,
    )
    interaction.followup.send.assert_awaited_once_with(
        "NEVER CLICK ON RANDOM BUTTONS THAT 'GUARANTEE' FREE STUFF ON THE INTERNET.",
        ephemeral=True,
    )

if __name__ == "__main__":
    test_freenitro()

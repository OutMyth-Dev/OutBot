from unittest.mock import AsyncMock, MagicMock

import pytest

from cogs import FreeNitroButton, FunCommands


@pytest.mark.asyncio
async def test_freenitro() -> None:
    """
    Tests if the command /freenitro sends "view=FreeNitroButton()". (/freenitro)

    Args:
        None

    Returns:
        None
    """
    fun_cog = FunCommands(MagicMock())

    view = FreeNitroButton()

    interaction = MagicMock()
    interaction.response.send_message = AsyncMock()

    await fun_cog.freenitro.callback(fun_cog, interaction)

    view = interaction.response.send_message.await_args.kwargs["view"]

    assert isinstance(view, FreeNitroButton)


@pytest.mark.asyncio
async def test_freenitro_button() -> None:
    """
    Tests if when the button is clicked it sends a gif and a warning. (/freenitro)

    Args:
        None

    Returns:
        None
    """
    view = FreeNitroButton()

    button_interaction = MagicMock()
    button_interaction.response.send_message = AsyncMock()
    button_interaction.followup.send = AsyncMock()

    button = view.children[0]

    await button.callback(button_interaction)

    button_interaction.response.send_message.assert_awaited_once_with(
        "https://tenor.com/view/rick-roll-nitro-gif-21997352",
        ephemeral=True,
    )
    button_interaction.followup.send.assert_awaited_once_with(
        "NEVER CLICK ON RANDOM BUTTONS THAT 'GUARANTEE' FREE STUFF ON THE INTERNET.",
        ephemeral=True,
    )


if __name__ == "__main__":
    test_freenitro()

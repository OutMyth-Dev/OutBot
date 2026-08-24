import discord
import logging
import os

from extensions import cogs
from discord.ext import commands
from dotenv import load_dotenv

# |===============|
# | Discord cofig |
# |===============|

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")
if not discord_token:
    raise RuntimeError("Discord token not found. Please enter you discod bot's token.")

handler = logging.FileHandler(
    filename="discord.log",
    encoding="utf-8",
    mode="a",
)

# |======|
# | Cogs |
# |======|

class OutBot(commands.Bot):

    async def setup_hook(self):
        for cog in cogs:
            await self.load_extension(cog)


# |========|
# | Intents|
# |========|

intents = discord.Intents.default()

bot = OutBot(
    command_prefix=None,
    intents=intents
)

# |======|
# |Events|
# |======|

@bot.event
async def on_ready():

    synced = await bot.tree.sync()

    print("\nOutBot is ready.\n")
    print(f"Synced {len(synced)} /commands.")

bot.run(
    discord_token,
    log_handler=handler,
    log_level=logging.DEBUG,
)

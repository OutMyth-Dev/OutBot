import discord
import logging
import os

from discord.ext import commands
from extensions import extensions
from dotenv import load_dotenv

# |===============|
# | Discord cofig |
# |===============|

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    logging.exception("Discord token is none. Please enter you discord bot's token.")
    raise RuntimeError("Discord token not found. Please enter you discod bot's token.")
    print("Enter your discord bot's token.")

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
        for extension in extensions:
            await self.load_extension(extension)


# |=========|
# | Intents |
# |=========|

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

    commands_synced = await bot.tree.sync()

    print("\nOutBot is ready.\n")
    print(f"Synced {len(commands_synced)} /commands.")

# |===========|
# | Bot Start |
# |===========|

bot.run(
    DISCORD_TOKEN,
    log_handler=handler,
    log_level=logging.DEBUG,
)

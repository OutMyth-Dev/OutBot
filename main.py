import discord

import logging

import os

from config.intents import intents
from config.logging import log_handler, log_level
from config.prefixes import command_prefix

from discord.ext import commands
from dotenv import load_dotenv
from config.extensions import extensions

# |=======================|
# |-Discord Configuration-|
# |=======================|

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    logging.error(
    "Discord token is none."
    "Please enter you Discord bot's token."
)

    raise RuntimeError(
        "Discord token not found.\n"
        "Please enter you Discod bot's token."
)

    print("Enter your Discord bot's token.")

# |===========|
# |-Load Cogs-|
# |===========|

class OutBot(commands.Bot):

    async def setup_hook(self):
        for extension in extensions:
            await self.load_extension(extension)

# |==============================|
# |-Command Prefixes And Intents-|
# |==============================|

bot = OutBot(
    command_prefix=command_prefix, 
    intents=intents,
)

# |========|
# |-Events-|
# |========|

@bot.event
async def on_ready():

    commands_synced = await bot.tree.sync()

    print(f"\nOutBot is ready and has {len(commands_synced)} synced /commands.")

# |====================|
# |-Bot Initialization-|
# |====================|

bot.run(
    DISCORD_TOKEN,
    log_handler=log_handler,
    log_level=log_level,
)

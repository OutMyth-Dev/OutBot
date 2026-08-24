import discord
import logging
import os

from cogs import cogs
from discord.ext import commands
from dotenv import load_dotenv

# |===============|
# | Discord cofig |
# |===============|

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("Discord token not found.")

handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="a")

# |======|
# | Cogs |
# |======|

for cog in cogs:
    await bot.load_extention(cogs)

# |=========|
# | Intents |
# |=========|

intents = discord.Intents.default()
bot = outbot(command_prefix=None, intents=intents)

# |========|
# | Events |
# |========|

@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print()
    print("OutBot is ready.")
    print()
    print(f"Synced {len(synced)} /commands.")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)

import discord
import logging
import os


from discord.ext import commands
from dotenv import load_dotenv


# |======|
# | Cogs |
# |======|

class LoadCogs(commands.Bot):
    async def cogs(self):
        await bot.load_extension("cogs.fun")
        await bot.load_extension("cogs.general")
        await bot.load_extension("cogs.information")
        await bot.load_extension("cogs.links")
        await bot.load_extension("cogs.rules")


# |===============|
# | Discord cofig |
# |===============|


load_dotenv()
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise RuntimeError("Discord token not found.")


handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="a")


# |=========|
# | Intents |
# |=========|


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=None, intents=intents)

# |========|
# | Events |
# |========|


@bot.event
async def on_ready():
    synced = await bot.tree.sync()
    print()
    print("OutBot is ready to be used.")
    print()
    print(f"Synced {len(synced)} slash commands.")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)

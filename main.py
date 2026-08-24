import discord
import logging
import os


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


class outbot(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.fun")
        await self.load_extension("cogs.general")
        await self.load_extension("cogs.information")
        await self.load_extension("cogs.links")
        await self.load_extension("cogs.rules")


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
    print("OutBot is ready to be used.")
    print()
    print(f"Synced {len(synced)} /commands.")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)

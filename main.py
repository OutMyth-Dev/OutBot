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


# |=========|
# | Intents |
# |=========|


intents = discord.Intents.default()
bot = commands.Bot(command_prefix=None, intents=intents)


# |======|
# | Cogs |
# |======|


class OutOut(commands.Bot):
    async def setup_hook(self, bot):
        self.bot = bot

        await bot.load_extension("cogs.fun_commands")
        await bot.load_extension("cogs.general_commands")
        await bot.load_extension("cogs.information_commands")
        await bot.load_extension("cogs.links_commands")
        await bot.load_extension("cogs.rules_commands")


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

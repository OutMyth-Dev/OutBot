import discord
import logging

from discord.ext import commands

class FunCommands(commands.Cog):

    def __init__(
        self, 
        bot: commands.Bot
):

        self.bot = bot

    @discord.app_commands.command(
        name="rickroll",
        description="Don't do it...",
)
    async def rickroll(
        self,
        interaction: discord.Interaction
):

        """Sends a youtube link to rickroll the user."""
        
        try:
            await interaction.response.send_message(
                "CLICK ME ---> ||<https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1>||",
                ephemeral=True,
)
        
        except discord.HTTPException():
            logging.exception("Discord's API failed when using /rickroll")
            await interaction.followup.send("Discord's API failed.")
        
        except Exception:
            logging.exception("Unexpected error in /rickroll")
            
            if interaction.response.is_done():
                await interaction.followup.send("An unexpected error occurred when using /rickroll. Please open a ticket.",
            ephemeral=True
)
            else:
                await interaction.response.send_message("An unexpected error occurred when using /rickroll. Please open a ticket.",
            ephemeral=True
)

async def setup(bot):
    await bot.add_cog(FunCommands(bot))

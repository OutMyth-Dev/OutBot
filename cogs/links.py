import discord
import logging

from discord.ext import commands

class LinksCommands(commands.Cog):
    def __init__(
        self, bot: commands.Bot
):
        self.bot = bot


    @discord.app_commands.command(
        name="youtube",
        description="OutMyth's YouTube channel link",
)

    async def youtube(
        self, 
        interaction: discord.Interaction
):
        try:
            await interaction.response.send_message(f"""OutMyth's YouTube Channel:
    
    <https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw>
    {interaction.user.mention}""")
        except discord.HTTPException:
            logging.exception("Discord's API failed when using /youtube")
            
            if interaction.response.is_done():
                await interaction.followup.send("Discord API failed when using /outmythrules.",
                ephemeral=True
)
            else:
                await interaction.response.send_message("Discord API failed when using /outmythrules",
                ephemeral=True
)

        except Exception:
            logging.exception("Unexpected errir in /youtube")
            
            if interaction.response.is_done():
                await interaction.followup.send("An unexpected error occurred when using when using /youtube. Please open a ticket.",
                ephemeral=True
)
            else:
                await interaction.response.send_message("An unexpected error occurred when using when using /youtube. Please open a ticket.",
                ephemeral=True
)

    @discord.app_commands.command(
        name="serverlink", 
        description="OutMyth's Discord server invite link."
)

    async def serverlink(self, 
    interaction: discord.Interaction
):

        try:
            await interaction.response.send_message(f"""OutMyth's Discord Server:

    https://discord.gg/Sc5vAvTJtc
    {interaction.user.mention}""")

        except discord.HTTPException:
            logging.exception("Discord's API failed when using /serverlink")
            
            if interaction.response.is_done():
                await interaction.followup.send("Discord API failed when using /serverlink.",
                ephemeral=True
)
            else:
                await interaction.response.send_message("Discord API failed when using /serverlink",
                ephemeral=True
)

        except Exception:
            logging.exception("Unexpected errir in /youtube")
            
            if interaction.response.is_done():
                await interaction.followup.send("An unexpected error occurred when using when using /serverlink. Please open a ticket.",
                ephemeral=True
)
            else:
                await interaction.response.send_message("An unexpected error occurred when using when using /serverlink. Please open a ticket.",
                ephemeral=True
)



    @discord.app_commands.command(
        name="invite",
        description="Invite link for OutBot",
)
    async def invite(
        self, 
        interaction: discord.Interaction
):
        try:
            await interaction.response.send_message(f"""Outbot Invite Link:
    
        <https://discord.com/oauth2/authorize?client_id=1525595736706781384>
    
        {interaction.user.mention}""")
        except discord.HTTPException:
            logging.exception("Discord's API failed when using /invite")
            
            if interaction.response.is_done():
                await interaction.followup.send("Discord API failed when using /invite.",
                ephemeral=True
)
            else:
                await interaction.response.send_message("Discord API failed when using /invite",
                ephemeral=True
)

        except Exception:
            logging.exception("Unexpected errir in /youtube")
            
            if interaction.response.is_done():
                await interaction.followup.send("An unexpected error occurred when using when using /invite. Please open a ticket.",
                ephemeral=True
)
            else:
                await interaction.response.send_message("An unexpected error occurred when using when using /invite. Please open a ticket.",
                ephemeral=True
)

async def setup(bot):
    await bot.add_cog(LinksCommands(bot))

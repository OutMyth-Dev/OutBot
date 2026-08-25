import discord
import logging

from discord.ext import commands

class LinksCommands(commands.Cog):

    @discord.app_commands.command(
        name="youtube",
        description="OutMyth's YouTube channel link",
)

    async def youtube(
        self, 
        interaction: discord.Interaction,
) -> None:

        try:
            await interaction.response.send_message(
                "# OutMyth's YouTube Channel:\n\n"
    
                "<https://www.youtube.com/channel/UCGjkPP8sjN8WanIY6hhAeKw>\n\n"
                
                f"{interaction.user.mention}"
)
        except discord.HTTPException:
            logging.exception("Discord's API failed when using /youtube")
            
            if interaction.response.is_done():
                await interaction.followup.send(
                    "Discord API failed when using /youtube.",
                    ephemeral=True,
)
            else:
                await interaction.response.send_message("Discord API failed when using /youtube",
                ephemeral=True,
)

        except Exception:
            logging.exception("Unexpected error in /youtube")
            
            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using when using /youtube. "
                    "Please open a ticket.",
                    ephemeral=True,
)
            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using when using /youtube. "
                    "Please open a ticket.",
                    ephemeral=True,
)

    @discord.app_commands.command(
        name="serverlink", 
        description="OutMyth's Discord server invite link.",
)

    async def serverlink(
        self, 
        interaction: discord.Interaction,
) -> None:

        try:
            await interaction.response.send_message(
                "# OutMyth's Discord Server:\n\n"

                "https://discord.gg/Sc5vAvTJtc\n\n"
                
                f"{interaction.user.mention}"
)

        except discord.HTTPException:
            logging.exception("Discord's API failed when using /serverlink")
            
            if interaction.response.is_done():
                await interaction.followup.send(
                    "Discord API failed when using /serverlink.",
                    ephemeral=True,
)
            else:
                await interaction.response.send_message(
                    "Discord API failed when using /serverlink",
                    ephemeral=True,
)

        except Exception:
            logging.exception("Unexpected error in /youtube")
            
            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using when using /serverlink. "
                    "Please open a ticket.",
                    ephemeral=True,
)
            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using when using /serverlink. "
                    "Please open a ticket.",
                    ephemeral=True,
)

    @discord.app_commands.command(
        name="invite",
        description="Invite link for OutBot",
)
    async def invite(
        self, 
        interaction: discord.Interaction,
) -> None:

        try:
            await interaction.response.send_message(
                f"Outbot Invite Link:\n\n"
    
                "<https://discord.com/oauth2/authorize?client_id=1525595736706781384>\n\n"
    
                f"{interaction.user.mention}"
)

        except discord.HTTPException:
            logging.exception("Discord's API failed when using /invite")
            
            if interaction.response.is_done():
                await interaction.followup.send(
                    "Discord API failed when using /invite.",
                    ephemeral=True,
)
            else:
                await interaction.response.send_message(
                    "Discord API failed when using /invite",
                    ephemeral=True,
)

        except Exception:
            logging.exception("Unexpected error in /youtube")
            
            if interaction.response.is_done():
                await interaction.followup.send(
                    "An unexpected error occurred when using when using /invite. "
                    "Please open a ticket.",
                    ephemeral=True,
)
            else:
                await interaction.response.send_message(
                    "An unexpected error occurred when using when using /invite. "
                    "Please open a ticket.",
                    ephemeral=True,
)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LinksCommands(bot))

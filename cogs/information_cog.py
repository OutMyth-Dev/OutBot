import logging


import discord
from discord.ext import commands


from config import (
    BOT_VERSION,
    DATE_CREATED,
    DEVELOPERS,
    GITHUB_LINK,
    LAST_MAJOR_UPDATED,
)


class InformationCommands(commands.Cog):


    @discord.app_commands.command(
        name="help",
        description="OutBot's Command Guide",
    )
    async def help(
        self,
        interaction: discord.Interaction,
    ) -> None:

        try:
            embed_message = discord.Embed(
                title=None,
                description=None,
            )
            embed_message = discord.Embed(
                title="📋 OutBot's Command List\n\n",
                description=(
                    "🎉 Fun ommands\n\n"
                    "- **/rickroll** - Sends a youtube link to rickroll you.\n\n"
                    "⚙️ General Commands\n\n"
                    "- 👋 /hello - Says hello to the user\n"
                    "- ✉️ /dm - DMs the user\n"
                    "- 🗣️ /say - You tell the bot what to say!\n"
                    "- 📊 /poll - Creates a poll\n\n"
                    "🧠 Information Commands\n\n"
                    "- ❓ /help - Command Guide\n"
                    "- 🤖 /outbot - Useful information about OutBot.\n"
                    "- 🗺️ /roadmap - OutBot's planned features\n\n"
                    "🔗 Links Commands\n\n"
                    "- ▶️ /youtube - OutMyth's YouTube channel link\n"
                    "- 💬 /serverlink - OutMyth's D iscord server invite link\n"
                    "- 🔗 /invite - OutBot's invite link**\n\n"
                    "⚖️ Rules Commands\n\n"
                    "- 📖 outmythrules - OutMyth's Rules\n"
                    "- 📄 outbotrules - OutBot's Rules",
                ),
                colour="0x5865F2"
            ),
            embed_message.set_footer(
                text="For more information, please open a ticket."
            )

            await interaction.response.send_message(embed=embed_message)

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /help",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /help."
            )

        except Exception:
            logger.exception("Unexpected error in /help")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="outbot",
        description="Useful Information About OutBot!",
    )
    async def outbot(self, interaction: discord.Interaction) -> None:

        try:
            embed_message = discord.Embed(
                title="🤖 OutBot\n\n',
                description=(
                    f"- {BOT_VERSION}\n"
                    f"- {CREATED_DATE}\n"
                    f"- {LAST_MAJOR_UPDATED}\n"
                    f"- {GITHUB_LINK}\n"
                    f"- {DEVELOPERS}\n\n" 
                ),
                colour=0x7289DA
            )

            await interaction.response.send_message(embed=embed_message)

        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /outbot",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /outbot."
            )

        except Exception:
            logger.exception("Unexpected error in /outbot")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )


    @discord.app_commands.command(
        name="roadmap",
        description="Planned Features For OutBot!",
    )
    async def roadmap(self, interaction: discord.Interaction) -> None:

        try:
            embed_message = discord.Embed(
                title="OutBot's Planned Features!\n\n",
                description=(
                    "- Assign/Remove Onboarding rolesn"
                    "- Improved Error Handlingn"
                    "- TOS & Privacy Policyn"
                    "- Bot Settings Commandsn"
                    "- Role Informationn"
                    "- Improved Quality Of Existing Commands"
                ),
            )
            
            await interaction.response.send_message(embed=embed_message)
            
        except discord.HTTPException:
            logger.exception(
                "Discord's API failed when using /roadmap",
            )
            await send_error_message(
                interaction, "Discord's API failed when using /roadmap."
            )

        except Exception:
            logger.exception("Unexpected error in /roadmap")

            await send_error_message(
                interaction, "Something went wrong :(. Please open a ticket."
            )
            

async def setup(bot: OutBot) -> None:
    await bot.add_cog(InformationCommands(bot))

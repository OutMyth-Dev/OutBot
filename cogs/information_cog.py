import discord
from discord.ext import commands

from config import (
    BOT_VERSION,
    CREATED_DATE,
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
            await interaction.response.send_message(
                "# 📋 OutBot's Command List\n\n"
                "## 🎉 Fun ommands\n\n"
                "- **/rickroll** - Sends a youtube link to rickroll you.\n\n"
                "## ⚙️ General Commands\n\n"
                "- ** 👋 /hello** - Says hello to the user\n"
                "- ** ✉️ /dm** - DMs the user\n"
                "- ** 🗣️ /say** - You tell the bot what to say!\n"
                "- ** 📊 /poll** - Creates a poll\n\n"
                "## 🧠 Information Commands\n\n"
                "- ** ❓ /help** - Command Guide\n"
                "- ** 🤖 /outbot** - Useful information about OutBot.\n"
                "- ** 🗺️ /roadmap** - OutBot's planned features\n\n"
                "## 🔗 Links Commands\n\n"
                "- ** ▶️ /youtube** - OutMyth's YouTube channel link\n"
                "- ** 💬 /serverlink** - OutMyth's D iscord server invite link\n"
                "- ** 🔗 /invite** - OutBot's invite link**\n\n"
                "## ⚖️ Rules Commands\n\n"
                "- ** 📖 outmythrules** - OutMyth's Rules\n"
                "- ** 📄 outbotrules** - OutBot's Rules"
            )

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
            await interaction.response.send_message(
                "## 🤖 OutBot\n\n"
                f"## - {BOT_VERSION}\n"
                f"## - {CREATED_DATE}\n"
                f"## - {LAST_MAJOR_UPDATED}\n"
                f"## - {GITHUB_LINK}\n"
                f"## - {DEVELOPERS}\n\n"
            )

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
            await interaction.response.send_message(
                "## OutBot's Planned Features!\n\n"
                "- **Assign/Remove Onboarding roles**\n"
                "- **Improved Error Handling**\n"
                "- **TOS & Privacy Policy**\n"
                "- **Bot Settings Commands**\n"
                "- **Role Information**\n"
                "- **Improved Quality Of Existing Commands**"
            )
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


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InformationCommands(bot))

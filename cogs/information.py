import discord

from discord.ext import commands

class InformationCommands(commands.Cog):

    @discord.app_commands.command(
        name="help",
        description="OutBot's Command Guide",
)
    async def help(
        self, 
        interaction: discord.Interaction,
) -> None:
        await interaction.response.send_message(
            "# 📋 OutBot's Command List\n\n"

            "## 🎉 Fun Commands\n\n"
            
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
            "- ** 🔗 /invite - OutBot's invite link**\n\n"

            "## ⚖️ Rules Commands\n\n"

            "- ** 📖 outmythrules** - OutMyth's Rules\n"
            "- ** 📄 outbotrules** - OutBot's Rules \n\n"

            f"{interaction.user.mention}"
)

    @discord.app_commands.command(
        name="outbot",
        description="Useful Information About OutBot!",
)

    async def outbot(
        self, interaction: discord.Interaction
) -> None:

        await interaction.response.send_message(
            "## 🤖 OutBot\n\n"

            "## - Bot Version = 0.4\n"
            "## - Developers = mythordian & aardappel1\n"
            "## - Date Started = July 11th 2026\n"
            "## - Last update = July 28nd 2026\n"
            "## - GitHub = <https://github.com/OuyMyth-Dev/OutBot/>\n\n"
            
            f"## - {interaction.user.mention}"
)

    @discord.app_commands.command(
        name="roadmap",
        description="Planned Features For OutBot!",
)

    async def roadmap(
        self, 
        interaction: discord.Interaction
)  -> None:

        await interaction.response.send_message(

            "## OutBot's Planned Features!\n\n"

            "- **Assign/Remove onboarding roles**\n"
            "- **Error handling**\n"
            "- **TOS & Privacy Policy**\n"
            "- **Bot Settings Commands**\n"
            "- **Role Information**\n"
            "- **Improved Quality Of Existing Commands**\n\n"

            f"{interaction.user.mention}"
)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InformationCommands(bot))

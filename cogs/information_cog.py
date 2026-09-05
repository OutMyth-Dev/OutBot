import discord
from discord.ext import commands

from config import (
    BOT_VERSION,
    CODE_OF_CONDUCT,
    CONTRIBUTING_POLICY,
    DATE_CREATED,
    DEVELOPERS,
    GITHUB_LINK,
    LAST_MAJOR_UPDATED,
    OUTBOT_INVITE_LINK,
    OUTBOT_LICENSE,
    PRIVACY_POLICY,
    RETENTION,
    SECURITY_POLICY,
    TERMS_OF_SERVICE,
)


class InformationCommands(commands.Cog):
    """
    General infomration about OutBot/OutMyth.

    Attributes:
        None

    Methords:
        help: OutBot's command guide.
        about: General information about OutBot.
        roadmap: OutBot's planned features.
    """

    @discord.app_commands.command(
        name="help",
        description="OutBot's Command Guide",
    )
    async def help(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot's command guide.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        embed_message = discord.Embed(
                title="📋 OutBot's Command List\n\n",
                description=(
                    "# 💻 Developer Commands\n\n"
                    "- **/developers**: Who are OutBot's developers?\n\n"
                    "# 🎉 Fun Commands\n\n"
                    "- **/freenitro**: Click a button that rickrolls you.\n"
                    "- **/freenitro**: Allows users to fakeban anyone!\n\n"
                    "# ⚙️ General Commands\n\n"
                    "- **/hello**: Says hello to the user.\n"
                    "- **/dm** - OutBot DMs you.\n"
                    "- **/ehco**: You tell the bot what to say!\n"
                    "- **/ping**: Click a button that pings you!\n"
                    "- **/poll**: Creates an embed with 10 default reactions.\n\n"
                    "# 🧠 Information Commands\n\n"
                    "-  **/help**: OutBot's Command Guide.\n"
                    "- **/outbot**: Useful information about OutBot.\n"
                    "- **/roadmap**: OutBot's planned features.\n\n"
                    "# 🔗 Links Commands\n\n"
                    "- **/youtube**: OutMyth's YouTube channel link.\n"
                    "- **/discord**: OutMyth's Discord server invite link.\n"
                    "- **/invite**: OutBot's invite link.**\n\n"
                    "# ⚖️ Rules Commands\n\n"
                    "- **outmythrules**: OutMyth's Rules.\n"
                    "- **outbotrules**: OutBot's Rules.\n\n"
                    "# 🙋‍♂️ Support Commands\n\n"
                    "- **/reporthelp**: Teaches you how to create a good report.\n"
                    "- **/report**: Report an issue. Including security related ones.\n"
                    "- **feedbackhelp**: Teaches you how to create good feedback.\n"
                    "- **feedback**: Give feeback to OutBot's developers.\n"
                ),
                # 0x5865F2 is Blurple
                colour=0x5865F2,
        )

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="about",
        description="Useful Information About OutBot!",
    )
    async def about(self, interaction: discord.Interaction) -> None:
        """
        General information about OutBot.

        Args:
            interactin (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        embed_message = discord.Embed(
            title="About: ",
            description=(
                "# Useful Information:\n\n"
                f"- Bot Version: v{BOT_VERSION}\n"
                f"- Log Retention: **{RETENTION}**\n"
                f"- GitHub: {GITHUB_LINK}\n"
                f"- Invite Link: {OUTBOT_INVITE_LINK}\n"
                f"- License: {OUTBOT_LICENSE}\n"
                f"- Privacy Policy: {PRIVACY_POLICY}\n"
                f"- Security policy: {SECURITY_POLICY}\n"
                f"- TOS: {TERMS_OF_SERVICE}\n"
                f"- Contributing Policy: {CONTRIBUTING_POLICY}\n"
                f"- Code Of Conduct: {CODE_OF_CONDUCT}\n"
            ),
            # 0x5865F2 is Blurple
            colour=0x5865F2,
        )
        embed_message.add_field(
            name="OutBot",
            value="Outbot is a general utility bot that takes user privacy and security seriously. Most discord bots do not. You can find out more via the links above.",
        )
        embed_message.set_footer(
            text=f"OutBot was made with python using discord.py. OutBot was developed by {DEVELOPERS}",
        )

        await interaction.response.send_message(embed=embed_message)

    @discord.app_commands.command(
        name="roadmap",
        description="Planned Features For OutBot!",
    )
    async def roadmap(self, interaction: discord.Interaction) -> None:
        """
        Features OutBot will get in future updates.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        embed_message = discord.Embed(
            title="OutBot's Planned Features!",
            description=(
                "# Next Update: \n"
                "- Bot Settings Commands\n"
                "- Role Information\n"
                "- Improved Quality Of Existing Commands\n"
                "- Diagnostic command (checking OutBot's config)\n"
                "- Improved documentation\n"
            ),
            # 0x2ECC71 is Emerald Green
            colour=0x2ECC71,
        )

        await interaction.response.send_message(embed=embed_message)


async def setup(bot: OutBot) -> None:
    await bot.add_cog(InformationCommands(bot))

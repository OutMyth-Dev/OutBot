import discord
from discord.ext import commands


class RulesCommands(commands.Cog):
    """
    Commands related to rules. Users can use to commands to find out rules they did not know about

    Attributes:
        None

    Methords:
        outmythrules: OutMyth's Discord server rules
        outbotrules: OutBot's rules
    """

    @discord.app_commands.command(
        name="outmythrules",
        description="OutMyth's Discord Server Rules.",
    )
    async def outmythrules(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutMyth's Discord server rules.

        Args:
            interaction (discord.Interaction): The Discord commamnd being invoked.

        Returns:
            None
        """
        # These can be found in the channel "rules", in OutMyth's Discord server.

        await interaction.response.send_message(
            "# 📜 OutMyth's Rules :\n\n"
            "# 1) ❌ NO NSFW And NO Malicious Content\n"
            "- Absolutely **NO** NSFW content, pornography, sexual content, or malicious links.\n\n"
            "# 2) 🤬 NO Swearing / Offensive Language\n"
            "- Use common sense when chatting.\n"
            "- Do **NOT** use censored words or other offensive language.\n\n"
            "# 3) 🔐 Respect Privacy\n"
            "- Do **NOT** dox or share anyone’s personal information.\n"
            "- Do **NOT** DM anyone without a valid reason.\n\n"
            "# 4) 🗣📢 No Self Promotion\n"
            "- **NO** advertising in DMs or channels.\n"
            "- This applies to EVERYONE, including staff and owners.\n\n"
            "# 5) @️ Use Mentions Responsibly And Lessange Spam\n\n"
            "- **DON’T** ping @everyone, @here, or use any other type of mass pinging or message spam.\n\n"
            "# 6) 🎟️ Tickets\n"
            "- Do NOT open tickets without a valid reason.\n\n"
            "# 7) 🫂 Behaviour\n"
            "- Be kind, respectful, and helpful to everyone.\n"
            "- Avoid disruptive behaviour. This includes malicious, manipulative, rage-baiting, or otherwise disruptive behaviour."
        )

    @discord.app_commands.command(
        name="outbotrules",
        description="OutBot's Rules!",
    )
    async def outbotrules(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """
        OutBot's rules.

        Args:
            interaction (discord.Interaction): The Discord command being invoked.

        Returns:
            None
        """
        await interaction.response.send_message(
            "## OutBot Rules\n\n"
            "- 1. Use the bot for its intended purpose.\n"
            "- 2. Only use OutBot in the channels command or chatbot.\n"
            "- 3. Do NOT try to exploit OutBot.\n"
            "- 4. Try to find bugs and report them by opening a ticket/report/PRIVATE GitHub reporting.\n"
        )


async def setup(bot: OutBot):
    await bot.add_cog(RulesCommands(bot))

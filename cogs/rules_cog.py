import discord
from discord.ext import commands


class RulesCommands(commands.Cog):
    @discord.app_commands.command(
        name="outmythrules",
        description="OutMyth Discord Server Rules.",
    )
    async def outmythrules(
        self,
        interaction: discord.Interaction,
    ) -> None:
        """These can be found in the channel "rules", in OutMyth's Discord server."""

        await interaction.response.send_message(
            "## :scroll: **Rules**\n\n"
            "## 1. :x:** NO** NSFW And **NO** Malicious Content.\n\n"
            "- :underage: Absolutely **NO** NSFW content, pornography, sexual content, or malicious links.\n\n"
            "## 2. :x: **NO** Swearing / Offensive Language\n\n"
            "- :speaking_head: Use common sense when chatting.\n\n"
            "- :no_entry_sign: Check out Censored Words.\n\n"
            "## 3. :white_check_mark: Respect Privacy\n\n"
            "- :lock: Do **NOT** dox or share anyone’s personal information.\n\n"
            "- :mailbox_with_mail: Do **NOT** Dm anyone without a valid reason.\n\n"
            "## 4. :x: No Self Promotion\n\n"
            "- :loudspeaker: **NO** advertising in Dms or channels.\n\n"
            "- :no_entry_sign: This applies to **EVERYONE**, including staff and owners.\n\n"
            "## 5. :white_check_mark: Use Mentions Responsibly\n\n"
            "#- :zap: **DON’T** ping @everyone; @here; any other types of mass pinging or message spam.\n\n"
            "## 6. :ticket: Tickets\n\n"
            "- :tickets: Do **NOT** open tickets without a valid reason.\n\n"
            "## 7. :people_hugging:  Behaviour\n\n"
            "- :handshake: Be kind, respectful, and helpful to everyone."
        )

    @discord.app_commands.command(
        name="outbotrules",
        description="OutBot's Rules!",
    )
    async def outbotrules(
        self,
        interaction: discord.Interaction,
    ) -> None:

        await interaction.response.send_message(
            "## Bot Rules\n\n"
            "- 1. Use the bot for its intended purpose.\n"
            "- 2. Only use OutBot in the channels command or chatbot.\n"
            "- 3. Do NOT try to exploit OutBot.\n"
            "- 4. Try to find bugs and report them by opening a ticket/report/PRIVATE GitHub reporting.\n"
        )


async def setup(bot: OutBot):
    await bot.add_cog(RulesCommands(bot))

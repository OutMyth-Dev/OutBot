# OutBot

OutBot is a Discord bot created by **Mythordian**, using **Discord.py**.OutBot is a general utility Discord bot that takes privacy and security seriously. **OutBot is 100% open source**. Most Discord bots like Echo, Security, and Ticketsv2 are **NOT**
open source. Open Source helps users understand what they are using while allowing them to do whatever they want to do with the project (depending on the license). It can also help make your project become a lot better. Take the kernel for instance, if it were closed source, it would be nowhere near as good as it is now.

OutBot's Current Version: **v0.4**

---

# Useful Link

OutBot's TOS
```text
https://github.com/OutMyth-Dev/OutBot/blob/main/TERMS.md
```

OutBot's Privacy Policy
```text
https://github.com/OutMyth-Dev/OutBot/blob/main/PRIVACY.md
```

OutBot's Security Policy
```text
https://github.com/OutMyth-Dev/OutBot?tab=security-ov-file
```

OutBot's License (MIT)
```text
https://github.com/OutMyth-Dev/OutBot/?tab=MIT-1-ov-file
```

OutBot's Invite link
```text
https://discord.com/oauth2/authorize?client_id=1525595736706781384
```

---

# What Are ephemeral Messages?

> Some messages can only be seen by the user who triggered the command.(ephemeral=True)
> Most messages can be seen by everyone. (ephemeral=False by default).
> The following commands are some examples of ephemeral=True commands:

- **`/dm`**
- **`/help`**
- **`/freenitro`**

> Error messages from the bot are all ephemeral=True.

---

# Built With

- **Python**
- **Discord.py**

---

# OutBot's Commands

OutBot does **NOT** use prefix  commands. Therefore, command_prefix=None. OutBot currently has 20+ slash commands.

OutBot's Config:
```py
bot = OutBot(
    command_prefix=None,
    intents=discord.Intents.default(),
)
```

---

# How do I install OutBot?

## Requirements

- Python 3.14.6 (https://www.python.org/downloads/)
- discord.py 2.7.1
- git (Install link - https://git-scm.com/install/)

base.txt:
```text
discord.py==2.7.1
python-dotenv==1.2.3
```
developer.txt
```text
ruff==0.16.6
cloc==0.2.5
```

test.txt
```text
dpytest==0.0.22
pytest==9.1.1
pytest-asyncio==1.4.0
```

These can be found in the directory "requirements". Make sure your base.txt, developer.txt, and test.txt has them.

## Getting A Local Copy Of OutBot.

```shell
git clone https://github.com/OutMyth-Dev/OutBot.git
```

```shell
cd OutBot
```

## Creating A Virtual Environment

```shell
python -m venv .venv
```

macOS/Linix:
```shell
source .venv/bin/activate
```

Windows:
```shell
.venv\Scripts\Activate.ps1
```

```shell
pip install -r requirements/base.txt
```

You can decide if you want to use tests or ruff/cloc.

If you want to use tests:
```shell
pip install -r requirements/tests.txt
```

If you want to use ruff and cloc use:
```shell
pip install -r requirements/developer.txt
```

# Discord Setup

# WARNING

DO NOT SHARE YOUR DISCORD BOT TOKEN WITH ANYONE. IF YOU DO, YOU GIVE THEM ACCESS TO YOUR BOT. THEY CAN EVEN FIND YOU EMAIL WITH IT.

### Why Do We Need A Discord Bot Token?

You now have a local copy of OutBot on your computer. For OutBot to actually run, we will need a Discord Bot Token. 

### Discord Developer Portal Setup.

Head over to Discord Developer portal (https://discord.com/developers/applications) and sign in/create an account. Click "new application".  Name your bot and accept Discord's Developer TOS/Privacy Policy. 

### Creating .env

Create a new file called .env and make sure it is in .gitignore. Create a variable called DISCORD_TOKEN.

### Getting A Discord Token For Your Bot.

On Discord Developer portal, click "Bot" and then click "Reset Token". Click "Yes do it to" confirm. Copy your Discord token into the file ".env".

### Adding Your Bot To Your Apps/Server(s)

Go to the "Installation" tab (discord developer portal); copy the install link and paste the install link into your browser. Then, choose whether you want OutBot in your apps or if you would like to add OutBot to your server/s. 

# IMPORTANT NOTE

**IF YOU DO NOT ADD YOUR DISCORD BOT TOKEN TO ".env", A RUNTIME ERROR WILL BE RAISED.**

# "I just want OutBot in my discord server/add it to my apps".

To invite OutBot to your server(s)/add it to your apps, head over to this link:
```text
https://discord.com/oauth2/authorize?client_id=1525595736706781384
```

Then choose if you want OutBot to your Discord server(s) or to your apps.

---

# Developer notes

Thank **you** for using OutBot! ❤️

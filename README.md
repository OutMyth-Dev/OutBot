# OutBot

OutBot is a Discord bot created by **Mythordian**, using **Discord.py**. OutBot is a general utility Discord bot that takes privacy and security seriously. **OutBot is 100% open source**. Most Discord bots like Echo, Security, and Ticketsv2 are **NOT** open source. Open Source helps users understand what they are using while allowing them to do whatever they want to do with the project (depending on the license). It can also help make your project become a lot better. Take the kernel for instance, if it were closed source, it would be nowhere near as good as it is now.



OutBot's Current Version: **v0.5.3**

---

# Useful Link

[OutBot's TOS](https://github.com/OutMyth-Dev/OutBot/blob/main/TERMS.md)  

[OutBot's Privacy Policy](https://github.com/OutMyth-Dev/OutBot/blob/main/PRIVACY.md)  

[OutBot's Security Policy](https://github.com/OutMyth-Dev/OutBot?tab=security-ov-file)  

[OutBot's License](https://github.com/OutMyth-Dev/OutBot/?tab=MIT-1-ov-file)  

[OutBot's Invite link](https://discord.com/oauth2/authorize?client_id=1525595736706781384)  

---

# What Are ephemeral Messages?

> Some messages can only be seen by the user who triggered the command. (ephemeral=True)
> Most messages can be seen by everyone. (ephemeral=False by default).
> The following commands are some examples of ephemeral=True commands:

- **`/dm`**
- **`/help`**
- **`/freenitro`**

> Error messages from the bot are all ephemeral=True.

---

# Command prefixes and privileged intents.

OutBot does **NOT** use prefix  commands. Therefore, command_prefix=None. OutBot uses **NO** privileged intents. Therefore, intents=discord.Intents.default()

OutBot's Config:
```py
bot = OutBot(
    command_prefix="\0",
    intents=discord.Intents.default(),
)
```

---

# Getting Started

## Requirements

- Python 3.14.6 [Install Python](https://www.python.org/downloads/)
- discord.py 2.7.1
- git [Install link](https://git-scm.com/install/) 

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

macOS/Linux:
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

(Windows) If you want to use tests:
```shell
pip install -r requirements/tests.txt
```

(Windows) If you want to use ruff and cloc use:
```shell
pip install -r requirements/developer.txt
```

Use pip3 install... if you are on Linux/macOS.

### Why Do We Need A Discord Bot Token?

You now have a local copy of OutBot on your computer. For OutBot to actually run, we will need a Discord Bot Token. 
DO NOT SHARE YOUR DISCORD BOT TOKEN WITH ANYONE. IF YOU DO, YOU GIVE THEM ACCESS TO YOUR BOT. THEY CAN EVEN FIND YOUR EMAIL WITH IT.

### Discord Developer Portal Setup.

Head over to [Discord Developer portal](https://discord.com/developers/applications) and sign in/create an account. Click "new application". Name your bot and accept Discord's Developer TOS/Privacy Policy. 

### Creating .env

Create a new file called .env and make sure it is in .gitignore. Create a variable called DISCORD_TOKEN.

### Getting A Discord Token For Your Bot.

On Discord Developer portal, click "Bot" and then click "Reset Token". Click "Yes do it to" confirm. Copy your Discord token into the file ".env".

### Adding Your Bot To Your Apps/Server(s)

Go to the [Discord Developer portal Installation Tab](https://discord.com/developers/applications/installation); copy the install link and paste the install link into your browser. Then, choose whether you want OutBot in your apps or if you would like to add OutBot to your server/s. 

# IMPORTANT NOTE

**IF YOU DO NOT ADD YOUR DISCORD BOT TOKEN TO ".env", A RUNTIME ERROR WILL BE RAISED.**

# Adding OutBot to your apps/discord server/s

To invite OutBot to your server(s)/add it to your apps, head over to this link:

[OutBot's Invite Link](https://discord.com/oauth2/authorize?client_id=1525595736706781384&scope=bot%20applications.commands)

Then choose if you want OutBot to your Discord server(s) or to your apps.

---

# Developer notes

Thank **you** for using OutBot! ❤️

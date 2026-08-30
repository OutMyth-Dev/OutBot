# 🤖 OutBot

OutBot is a Discord bot created by **Mythordian** and **aardapel1**, built with **Discord.py**.
OutBot is a geneal utility discord bot with privacy and security in mind.

Current version: **0.4**

---

# 🔗 Useful link

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
https://github.com/OutMyth-Dev/OutBot/
```

OutBot Invite link
```text
https://discord.com/oauth2/authorize?client_id=1525595736706781384
```

---

# 🔒 What are Ephemeral Messages?

Some messages can **only be seen by the user who triggered the command**.*(Ephemeral=True)
**Most** messages can be seen by everyone (Ephemeral=False by default).
The following commands have Ephemeral=True:

- **`/dm`**
- **`/help`**
- **`/freenitro`**

> Error messages from the bot are all Ephemeral=True.

---

# 🛠️ Built With

- **Python**
- **Discord.py**

---

# 🤖 OutBot Commands
OutBot currently has **20 slash commands**.
OutBot does **NOT** use  prefix  commands, so there is no command prefix required; as shown below.

```text
bot = OutBot(
    **command_prefix=None,**
    intents=discord.Intents.default(),
)
```

---

# ⚙️ Cogs
OutBot has **7 cogs**

| Cog relative file path| What types of commands the cog contains | An example of that command |
| --- | --- | --- |
| **cogs/fun_cog.py** | - Commands that exist for users to have fun | - eg: /rickroll |
| **cogs/general_cog.py** | - Commands that do not fit in any other category | - eg: /hello |
| **cogs/information_cog.py** |- Useful information about OutBot/OutMyth | - eg: /help |
| **cogs/links_cog.py** | - Useful links about OutBot/OutMyth | - eg: /youtube |
| **cogs/privacy_cog.py**| - User privacy information | -eg: /privacy |
| **cogs/rules_cog.py** |- OutBot/OutMyth's Rules | - eg: /outmythrules |
| **cogs/support_cog.py** | - User support commands. | -eg: /report |

---

### ❓ What commands does each cog contain?

### cogs/fun_cog.py

- **`/freenitro`**
- **`/fakeban`**

### cogs/general_cog.py

- **`/hello`**
- **`/dm`**
- **`/say`**
- **`/ping`**
- **`/poll`**

### cogs/information_cog.py

- **`/help`**
- **`/outbot`**
- **`/roadmap`**

### cogs/links_cog.py

- **`/youtube`**
- **`/serverlink`**
- **`/invite`**

### cogs/privacy_cog.py

- **`/privacy`**
- **`/data`**
- **`/logs`**

### cogs/rules_cog.py

- **`/outmythrules`**
- **`/outbotrules`**

### cogs/support_cog.py

- **`/reporthelp`**
- **`/report`**
- **`/feedback`**

---

# 🗂️ OutBot's Directory Tree

```text
OutBot/
├── cogs/
│   ├── fun_cog.py
│   ├── general_cog.py
│   ├── information_cog.py
│   ├── links_cog.py
|   ├── privacy_cog.py
│   ├── rules_cog.py
|   └── support_cog.py
├── config/
│   ├── __init__.py
│   ├── .env.example
|   ├── bot_info.py
│   ├── emojis.py
│   ├── load_cogs.py
│   ├── logging.py
│   └── max_chars.py
├── information/
│   ├── UPDATES.md
│   └── errors.py
│   utils/
│   ├── __init__.py
│   └── errors.py
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

---

# 🤔 How do I install OutBot?

---

## 📝 Requirements

- Python 3.14.6 (https://www.python.org/downloads/)
- discord.py 2.7.1
- git (Install link - https://git-scm.com/install/)
- A discord bot application (It depends on what you want to do with OutBot. Before creating one, please read the instructions below.)
- git (Install link - https://git-scm.com/install/)

```text
discord.py
dpytest
pytest
pytest-asyncio
python-dotenv
```

These can be found in the file requirements.txt. Make sure your requirements.txt has them

---

## ⬇️ Installing OutBot

**PLEASE MAKE SURE YOU HAVE GIT INSTALLED.**

Run the following command in your terminal to have a local copy of OutBot on your computer:

```text
git clone https://github.com/OutMyth-Dev/OutBot.git
```

And to switch to OutBot's directory:
```text
cd OutBot
```

To install all dependencies, run:
```text
pip install -r requirements.txt
```

---

# 🛠️ Discord Setup

---

## 🤫 .env

# DO NOT SHARE YOUR DISCORD BOT TOKEN WITH ANYONE. IF YOU DO, YOU GIVE THEM ACCESS TO YOUR BOT. THEY CAN EVEN FIND YOU EMAIL WITH IT.*

You now have a local copy of OutBot on your computer. To OutBot actually run we will need a Discord Bot Token. Head over to Discord
Developer portal (https://discord.com/developers/applications) and sign in/create an account depending on if you have a Discord account.
Click "new application". Create a name for your bot; accept Discord's Developer TOS/Privacy Policy. Create a new file called .env and make sure it is in 
.gitignre. Created a variable called DISCORD_TOKEN. Under overview click "Bot" and then click "Reset Token". Click "Yes do it to" confirm. Copy your Discord token into .env.Finally, to install it, go to the "Installation" tab; copy the install link. Paste the install link into your browser and choose if you want OutBot in your apps or if you want to add OutBot to your server/s. You can now do whatever you want to the source code. **PLEASE READ THE MIT LICENSE FOR MORE INFORMATION.** **IF YOU DO NOT ADD A DISCORD BOT TOKEN, YOU WILL GET A RUNTIME ERROR.**

MIT LICENSE:
```text
https://github.com/OutMyth-Dev/OutBot/
```

---

# 🧐 "I just want OutBot in my discord server/add it to my apps".

To invite OutBot to your server/add it to your apps, head over to this link:

```text
https://discord.com/oauth2/authorize?client_id=1525595736706781384
```

Then choose whether you want OutBot in your Discord server or in your apps.

---

To report an issue other than a security related one, 
please open a ticket on OutMyth https://discord.gg/Sc5vAvTJtc 
or a GitHub issue https://github.com/OutMyth-Dev/OutBot/issues.
Thank **you** for using OutBot! ❤️

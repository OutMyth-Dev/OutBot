# 🤖 OutBot

OutBot is a Discord bot created by **Mythordian** and **aardapel1**, built with **Discord.py**.
OutBot was created to replace other bots for privacy and security reasons.

Current version: **0.4**

---

## 🔐 Privacy

| Data | Collected | Stored | Retention |
| --- | --- | --- | --- |
| Message content | ❌ No | ❌ No | None |
| User data | ❌ No | ❌ No | None |
| Logs | ✅ Limited | ✅ Local | 7 days |

- Logs use a logging mode of **a** (append)
- OutBot is **open source**
- OutBot is under an MIT LICENSE: https://github.com/OutMyth-Dev/OutBot/blob/main/LICENSE

If you have any privacy concerns please open a GitHub issue on create a ticket on OutMyth's discord server.

---

# 🔒 What are Ephemeral Messages?

Some messages can **only be seen by the user who triggered the command**.*(Ephemeral=True)
**Most** messages can be seen by everyone (Ephemeral=False by default).
The following commands have Ephemeral=True:

- 📩 **`/dm`**
- 🆘 **`/help`**
- 🥸 **`/rickroll`**

> ⚠️ Error messages from the bot are all Ephemeral=True.

---

# 🛠️ Built With

- 🐍 **Python**
- 🤖 **Discord.py**

---

# 🤖 OutBot Commands
OutBot currently has **14 slash commands**.
OutBot does **not** use  prefix  commands, so there is no command prefix required.

---

# ⚙️ Cogs
OutBot has *5 cogs*

| Cog relative file path| What types of commands the cog contains | An example of that command |
| --- | --- | --- |
| **cogs/fun_cog.py** | - Commands that exist for users to have fun | - eg: /rickroll |
| **cogs/general_cog.py** | - Commands that do not fit in any other category | - eg: /hello |
| **cogs/information_cog.py** |- Useful information about OutBot/OutMyth | - eg: /help |
| **cogs/links_cog.py** | - Useful links about OutBot/OutMyth | - eg: /youtube |
| **cogs/rules_cog.py** |- OutBot/OutMyth's Rules | - eg: /outmythrules |

---

### ❓ What commands does each cog contain?

### cogs/fun.py

- **`/rickroll`**

### cogs/general.py

- **`/hello`**
- **`/dm`**
- **`/say`**
- **`/ping`**
- **`/poll`**

### cogs/information.py

- **`/help`**
- **`/outbot`**
- **`/roadmap`**

### cogs/links.py

- **`/youtube`**
- **`/serverlink`**
- **`/invite`**

### cogs/rules.py

- **`/outmythrules`**
- **`/outbotrules`**

# OutBot's Directory Tree

```text
OutBot/
├── cogs/
│   ├── fun.py
│   ├── general.py
│   ├── information.py
│   ├── links.py
│   └── rules.py
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

- Python 3.14.6
- discord.py 2.7.1
- git (Install link - https://git-scm.com/install/) 
- A discord bot application (It depends on what you want to do with OutBot.)

---

## ⬇️ Installing OutBot

PLEASE MAKE SURE YOU HAVE GIT INSTALLED.

Run the following command in your terminal:

```text
git clone https://github.com/OutMyth-Dev/OutBot.git
```

Then run:
```text
cd OutBot
```

To install all dependencies, run:
```text
pip install -r requirements.txt
```

# 🛠️ Discord Setup

---

## 🤫 .env

You now have a local copy of OutBot on your computer. To OutBot actually run we will need a Discord Bot Token. Head over to Discord
Developer portal (https://discord.com/developers/applications) and sign in/create an account depending on if you have a Discord account.
Click "new application". Create a name for your bot and accept Discord's Dev TOS/Privacy policy. Create a new file called .env and make sure it is in 
.gitignre. Created a variable called DISCORD_TOKEN. Under overview click "Bot" and then click"Reset Token". Click "Yes do it to" confirm; enter your 
password for authentication. Copy your Discord token into .env.Finally, to install it, go to "Installation" and copy the install link. Paste the install 
link into your browser and choose if you want toadd your bot to your apps or if you want to add them to your servers. You can now do whatever you want 
to the source code. Please read the MIT LICENSE for more information. NEVER SHARE YOUR DISCORD TOKEN WITH ANYONE. IF YOU DO, YOU ARE ALLLOWING THEM TO 
HAVE ACCESS TO YOUR BOT. THEY CAN ALSO FIND YOUR EMAIL WITH YOUR DISCORD BOT TOKEN.

---

## 🧐 I just want OutBot in my discord server/add it to my apps.

To invite OutBot to your server/add it to your apps, head over to this link: https://discord.com/oauth2/authorize?client_id=1525595736706781384.
Then choose whether you want OutBot in your Discord server; in your apps.

---

To report any issues, open a ticket on OutMyth - https://discord.gg/Sc5vAvTJtc or a GitHub issue - https://github.com/OutMyth-Dev/OutBot/issues.
Thank **you** for using OutBot! ❤️

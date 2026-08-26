# 🤖 OutBot

OutBot is a Discord bot created by **Mythordian** and **aardapel1** using **Discord.py**.
OutBot was created to replace other bots for privacy and security reasons. It is **not a moderation bot**.
A separate moderation bot called **OutMod** will be released in the near future.

--------------

# 🤖 OutBot Commands
OutBot currently has **14 slash commands**.
OutBot does **not** use prefix commands, so there is no command prefix required.

--------------

# 🔒 What are Ephemeral Messages?

Ephemeral messages can **only be seen by the user who triggered the command**.
When Ephemeral=True, **only the user who sent the command can see the message displayed by the bot**.
When Ephemeral=False, **everyone can see the message sent by the bot** (Ephemeral=Flase by default).
The following commands have Ephemeral=True:

- 📩 **`/dm`**
- 🆘 **`/help`**
- 🥸 **`/rickroll`**

> ⚠️ Error messages from the bot are all Ephemeral=True.

--------------

# 🛠️ Built With

- 🐍 **Python**
- 🤖 **Discord.py**

--------------

# 🚧 Future Projects

### 🛡️ OutMod

A separate Discord moderation bot is planned for the future.
OutMod will be a **moderation bot with user privacy in mind**. Whilst OutBot will focus on **everything except moderation**.

--------------

# 👥 Developers

- **mythordian**
- **aardapel1**

--------------

# ⚙️ Cogs
OutBot has *5 cogs*

- **cogs/fun.py**         | Commands that exists for users to have fun     | eg: /rickroll
- **cogs/general.py**     | Commands that do not fit in any other category | eg: /hello
- **cogs/information.py** | Useful information about OutBot/OutMyth        | eg: /help
- **cogs/links.py**       | Useful links about OutBot/OutmMyth             | eg: /youtube
- **cogs/rules.py**       | OutBot/OutMyth's Rules                         | eg: /outmythrules

### ❓ What commands does each cog contain?

### cogs/fun.py

- **`/rickroll`**

### cogs/general.py

- **`/hello`**
- **`/dm`**
- **`/say`**
- **`/poll`**

### cogs/information.py

- **`/help`**
- **`outbot`**
-**`/roadmap`**

### cogs/links.py

- **`/youtube`**
- **`severlink`**
- **`/invite`**

## cogs/rules.py

- **`outmythrules`**
- **`outbotrules`**

# OutBot's File structure

```text
OutBot/
├── cogs/
│   ├── fun.py
│   ├── general.py
│   ├── information.py
│   ├── links.py
│   └── rules.py
├── config/
│   ├── .env.example
|   ├── bot_info.py
│   ├── emojis.py
│   ├── extensions.py
│   ├── logging.py
│   ├── max_chars.py
│   └── prefixes.py
├── information/
│   └── UPDATES.md
├── .gitignore
├── discord.log
├── main.py
├── README.md
└── requirements.txt
```

To report any issues please open a ticket on OutMyth - https://discord.gg/Sc5vAvTJtc or, please open a GitHub issue.
**Thanks for using OutBot!**

# 🤖 OutBot

Current version: **0.4**

OutBot is a Discord bot created by **Mythordian** and **aardapel1**, built with **Discord.py**.
OutBot was created to replace other bots for privacy and security reasons.

- It does **not collect user data**. If any user data is collected it is only to **debug**.
- Logs are kept **local**.
- User data and logs are **deleted weekly**.
- Message content is **NOT** collected.

--------------

# 🤖 OutBot Commands
OutBot currently has **14 slash commands**.
OutBot does **not** use prefix commands, so there is no command prefix required.

--------------

# 🔒 What are Ephemeral Messages?

Some messages can **only be seen by the user who triggered the command**.*(Ephemeral=True)
**Most** messages can be seen by everyone (Ephemeral=False by default).
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

# ⚙️ Cogs
OutBot has *5 cogs*

- **cogs/fun.py**         | Commands that exist for users to have fun      | eg: /rickroll
- **cogs/general.py**     | Commands that do not fit in any other category | eg: /hello
- **cogs/information.py** | Useful information about OutBot/OutMyth        | eg: /help
- **cogs/links.py**       | Useful links about OutBot/OutMyth              | eg: /youtube
- **cogs/rules.py**       | OutBot/OutMyth's Rules                         | eg: /outmythrules

--------------

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
-**`/roadmap`**

### cogs/links.py

- **`/youtube`**
- **`serverlink`**
- **`/invite`**

### cogs/rules.py

- **`outmythrules`**
- **`outbotrules`**

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
│   └── __init__.py
├── .gitignore
├── LICENSE
├── main.py
├── README.md
└── requirements.txt
```

--------------

To report any issues, open a ticket on OutMyth - https://discord.gg/Sc5vAvTJtc or a GitHub issue - https://github.com/OutMyth-Dev/OutBot/issues.
Thank **you** for using OutBot!

# 🔧 Discord Bot Template

A clean and expandable **Python Discord bot template** using `discord.py` with support for automatic cog loading.

## 🚀 Features

* Easy-to-edit bot structure
* Automatic loading of cogs from the `./cogs` folder
* Example cog included
* Commands:

  * `!ping` — Check bot latency
  * `!uptime` — Shows how long the bot has been online

---

## 📁 Project Structure

```
📦 your-bot
├── main.py
├── cogs
│   ├── 1.py
│   └── (add more cogs here)
└── Requirements.txt
```

---

### 2. Add your bot token

Inside `main.py`:

```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
```

---

## ▶️ Running the bot

Run the main script:

```bash
python main.py
```

---

## 🧩 Creating a Cog

Put a file inside the `cogs` folder:

```python
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello from a cog!")

async def setup(bot):
    await bot.add_cog(Example(bot))
```

---

## 💬 Support

If you want more commands, features, or help setting up hosting, just ask!

---

## ⭐ Like this project?

Star it, share it, or expand it with your own cogs!

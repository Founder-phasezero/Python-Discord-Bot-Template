import discord
from discord.ext import commands
import os

# Replace with your bot's token
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Intents define what events your bot will receive
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs automatically from the ./cogs folder
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is ready!")

    # Auto-load cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cog: {filename}")

# Run the bot
bot.run(TOKEN)

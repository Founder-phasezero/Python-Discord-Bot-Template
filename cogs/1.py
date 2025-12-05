import time
from discord.ext import commands

start_time = time.time()

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Returns bot latency"""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! `{latency}ms`")

    @commands.command()
    async def uptime(self, ctx):
        """Shows how long the bot has been online"""
        current_time = time.time()
        total_seconds = int(current_time - start_time)

        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        await ctx.send(f"Uptime: `{hours}h {minutes}m {seconds}s`")

async def setup(bot):
    await bot.add_cog(Utility(bot))

import discord
from discord.ext import commands
from datetime import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(description="**Basic Commands 💈:**\n> ping - `Check the ping.`\n\n**Info Commands 📕 :**\n> covid [country] - `Display the covid stats from a specific country.`\n\n**Dev Commands 🛠️ :**\n> reload - `Reload a command.`", color=0x333438, title='💡 | Prefix: `-`')
        embed.set_author(name = f'Help Menu')
        #timestamp=datetime.utcnow()
        await ctx.send(embed = embed)
        #await msg.add_reaction('📀')


def setup(bot):
    bot.add_cog(Help(bot))

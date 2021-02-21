import discord
from discord.ext import commands
from Data.Api.dataManager import DataManager

class GetData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def getdata(self, ctx):

        DataManager.resetData(self.bot)
        schema = DataManager.getRawData()

        await ctx.send(f"""```{schema} ```""")


def setup(bot):
    bot.add_cog(GetData(bot))

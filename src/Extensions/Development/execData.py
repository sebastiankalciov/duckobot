import discord
from discord.ext import commands
from Data.Api.dataManager import DataManager

class ExecData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def testdata(self, ctx): # A test command.

        DataManager.setData(self.bot)
        rawdata = DataManager.getRawData()
        await ctx.send(f"https://cdn.discordapp.com/avatars/{self.bot.user.id}/{self.bot.user.avatar}")

    @commands.command()
    async def getdata(self, ctx): # A command to get raw data.

        DataManager.setData(self.bot)
        rawdata = DataManager.getRawData()
        print(self.bot.users)
        await ctx.send(f"""```{rawdata} ```""")


def setup(bot):
    bot.add_cog(ExecData(bot))

import discord
from discord.ext import commands
from Data.Api.dataManager import DataManager

class ExecData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def testdata(self, ctx):

        DataManager.resetData(self.bot)
        schema = DataManager.getRawData()
        await ctx.send(f"https://cdn.discordapp.com/avatars/{self.bot.user.id}/{self.bot.user.avatar}")

    @commands.command()
    async def getdata(self, ctx):

        DataManager.resetData(self.bot)
        schema = DataManager.getRawData()
        print(self.bot.users)
        await ctx.send(f"""```{schema} ```""")


def setup(bot):
    bot.add_cog(ExecData(bot))

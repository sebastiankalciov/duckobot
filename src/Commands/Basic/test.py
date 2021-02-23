import discord
from discord.ext import commands
from Library.Managers.languageManager import Language
class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def test(self, ctx):
        Language.addMessage("core", "test")
        print('testdad')


def setup(bot):
    bot.add_cog(Test(bot))

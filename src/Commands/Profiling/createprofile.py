import discord
from discord.ext import commands
from Library.Managers.LanguageManager import Language


class Createprofile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def createprofile(self, ctx, *args):

        if args == ():
            return await ctx.send(Language.getMessage("CreateProfile", "no_arg"))


def setup(bot):
    bot.add_cog(Createprofile(bot))

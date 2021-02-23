import discord
from discord.ext import commands
from Library.Managers.dataManager import DataManager # Importing Data Manager from Library directory.

class ExecData(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def testdata(self, ctx): # A test command.

        DataManager.setData(self.bot)
        rawdata = DataManager.getRawData()
        await ctx.send(f"https://cdn.discordapp.com/avatars/{self.bot.user.id}/{self.bot.user.avatar}")

    @commands.command()
    async def getdata(self, ctx, *args): # A command to get raw data.

        DataManager.setData(self.bot)
        rawdata = DataManager.getRawData()
        if args == ():
            await ctx.send(f"""```{rawdata} ```""")

        elif args[0].lower() == "avatar".lower():
            await ctx.send(rawdata["botAvatar"])

        elif args[0].lower() == "guilds".lower():
            await ctx.send(rawdata["guildSize"])
            
        else: # Displays all available options that can be get from <data.json>

            embed = discord.Embed(color=0xd14242)
            embed.set_author(name = "Available data options", icon_url= f"https://cdn.discordapp.com/avatars/{self.bot.user.id}/{self.bot.user.avatar}")
            embed.add_field(name="Avatar",value= "> Get the bot's avatar.")
            embed.add_field(name="Guilds",value= "> Get the number of guilds.")

            await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(ExecData(bot))

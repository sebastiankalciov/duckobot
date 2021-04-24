import discord
from discord.ext import commands
import glob

from discord.ext.commands.converter import ColourConverter
from Library.Managers.LanguageManager import Language
from Library.Util.EmbedGenerator import embf
from Library.Util.GetConfigData import getData

OWNER_ID = getData("owner_id")

class Cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cmd(self, ctx, args):

        if str(ctx.author.id) != OWNER_ID:

            return await ctx.send(embed = embf(Language.getMessage("Cmd", "no_perm"), color=0xd14242))

        posibileComenzi = glob.glob('./Commands/**/*.py')

        for fisier in posibileComenzi:
            try:

                if fisier.endswith('.py'):

                    if fisier[2:].replace('\\', '.')[:-3].split(".")[2] == args:

                        if fisier[2:].replace('\\', '.')[:-3].split(".")[2] == 'core':
                            break

                        with open(fisier, "r", encoding="utf-8") as file:

                            text = file.readlines()
                            embed = discord.Embed(description='```py\n{}```'.format('\n'.join(str(p) for p in text)), color = 0xd14242)
                            await ctx.send(embed = embed)
                            break

            except:

                break


def setup(bot):
    bot.add_cog(Cmd(bot))

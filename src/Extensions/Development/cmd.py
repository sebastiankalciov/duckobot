import discord
from discord.ext import commands
import glob


class Cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cmd(self, ctx, args):
        if ctx.author.id != 244396629220786177:
            await ctx.send('fut una la ochiada')
            return
        posibileComenzi = glob.glob('./Extensions/**/*.py')

        for fisier in posibileComenzi:
            try:
                if fisier.endswith('.py'):
                    if fisier[2:].replace('\\', '.')[:-3].split(".")[2] == args:
                        if fisier[2:].replace('\\', '.')[:-3].split(".")[2] == 'core':
                            await ctx.send('sa no fut eu pe mata')
                            break
                        with open(fisier, "r", encoding="utf-8") as file:
                            text = file.readlines()
                            embed = discord.Embed(description='```py\n{}```'.format('\n'.join(str(p) for p in text)))
                            await ctx.send(embed = embed)
                            break


            except:
                print('nu e ce trebuie')
                break


def setup(bot):
    bot.add_cog(Cmd(bot))

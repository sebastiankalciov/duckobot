import glob
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='-') # Initiating a bot with a custom prefix.
bot.remove_command('help') # Removing the help command to add a custom one.

import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
#from Data.Functions.reloadFunction import reload

@bot.event

async def on_ready(): # On ready event

    print(f'Ready <{bot.user.name}>')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="America"))

@bot.event

async def on_command_error(ctx, error): # Error handler

    if isinstance(error, commands.CommandNotFound):

        return

    if isinstance(error, commands.BadArgument):

        return

    if isinstance(error, commands.MissingRequiredArgument):

        return

    if isinstance(error, commands.MissingPermissions):

        return

    else:
        raise error



if __name__ == "__main__": # Running cogs

    possibleCommands = glob.glob('./Extensions/**/*.py')

    for file in possibleCommands:


        try:
            



            file.endswith('.py'):    

                bot.load_extension(file[2:].replace('\\', '.')[:-3])
                print("Cog pornit: " + str(file[2:].replace('\\', '.')[:-3].split(".")[2]))

        except Exception as e:

            exc = '{}: {}'.format(type(e).__name__, e)
            print('Eroare, cog problema: {}\n{}'.format(file, exc))


#@bot.command()
#async def reload(self, ctx):
#    await reload(self, ctx)


bot.run('NjYxMzEyOTgxMjkxNzYxNzAz.Xgpl2g.X14frzqHAzfxKELnDF1qI28EOag')

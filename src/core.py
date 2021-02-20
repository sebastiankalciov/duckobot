import glob
from discord.ext import commands
import discord
import json
import platform
bot = commands.Bot(command_prefix='-') # Initiating a bot with a custom prefix.
bot.remove_command('help') # Removing the help command to add a custom one.

import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

#from Data.Functions.reloadFunction import reload


data = json.load(open('./Data/JSON/config.json', "r"))
token = data["token"]


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
                        
            if file.endswith('.py'):    
                
                if platform.system() == "Linux":

                    bot.load_extension(file[2:].replace('/', '.')[:-3])

                    print("Cog stable: " + str(file[2:].replace('/', '.')[:-3].split(".")[2]))
                else:
                    bot.load_extension(file[2:].replace('\\', ".")[:3])
                    print("Cog stable: " + str(file[2:].replace("\\", ".")[:-3].split(".")[2]))

        except Exception as e:

            exc = '{}: {}'.format(type(e).__name__, e)
            print('Error, unstable cog: {}\n{}'.format(file, exc))


#@bot.command()
#async def reload(self, ctx):
#    await reload(self, ctx)


    bot.run(token)

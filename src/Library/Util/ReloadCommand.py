import glob # Importing required libraries and modules.
from discord.ext import commands
import discord
import json
import platform
from Library.Managers.LanguageManager import Language

async def ReloadCommand(self, ctx, bot):
    """## Reload command of duckobot

    Reloads a command.

    Parameters
    ----------

    self:  :class: :parameter:
            Parameter

    ctx:   :class: :variable:
            Parameter

    bot:   :class: :variable:
            Client
    
   
    """

    possibleCommands = glob.glob('./Commands/**/*.py')
    try:
        for file in possibleCommands:

            if file[2:].replace('\\', '.')[:-3].split(".")[2].lower() == ctx.lower():

                bot.unload_extension(file[2:].replace('\\', '.')[:-3])
                bot.load_extension(file[2:].replace('\\', '.')[:-3])

                embed = discord.Embed(description = Language.getMessage('ReloadCommand', "reloaded_successfully").replace("{ctx}", ctx), color=0x5fab38)
                return await self.send(embed = embed)

    except Exception as e:
        return await self.send(embed = discord.Embed(description= Language.getMessage('ReloadCommand', "reloaded_unsuccessfully").replace("{ctx}", ctx), color=0xd14242))
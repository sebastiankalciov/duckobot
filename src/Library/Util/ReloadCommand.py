import glob # Importing required libraries and modules.
from discord.ext import commands
import discord
import json
import platform


async def ReloadCommand(self, ctx, bot):
    possibleCommands = glob.glob('./Commands/**/*.py')
    try:
        for file in possibleCommands:

            if file[2:].replace('\\', '.')[:-3].split(".")[2].lower() == ctx.lower():

                bot.unload_extension(file[2:].replace('\\', '.')[:-3])
                bot.load_extension(file[2:].replace('\\', '.')[:-3])

                embed = discord.Embed(description=f'> Command `{ctx}` reloaded successfully! ✅', color=0x5fab38)
                return await self.send(embed = embed)

    except Exception as e:
        return await self.send(embed = discord.Embed(description=f'> Command `{ctx}` does not exist! ❌', color=0xd14242))
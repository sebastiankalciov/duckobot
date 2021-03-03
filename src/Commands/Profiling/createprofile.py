import discord
import asyncio
import asyncpg
from discord.ext import commands
from Library.Managers.LanguageManager import Language
from Library.Managers.DBManager import DBManager
from Library.Util.GetConfigData import getData
from Library.Util.EmbedGenerator import embf
from Library.Util.GenerateID import generateID
APPROVED_EMOJI = f"<:approved:{getData('emotes', 'approved')}>" # Emote One
REJECTED_EMOJI = f"<:rejected:{getData('emotes', 'rejected')}>" # Emote Two
db = DBManager()
usersDB = db.UsersManager()

class Createprofile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def createprofile(self, ctx, *args):

        if args == ():
            return await ctx.send(embed = embf(Language.getMessage("CreateProfile", "no_arg").replace("{{emoji}}", REJECTED_EMOJI)))

        
            
 

def setup(bot):
    bot.add_cog(Createprofile(bot))

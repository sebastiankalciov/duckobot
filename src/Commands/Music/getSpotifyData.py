from inspect import Attribute
import discord
from discord.ext import commands
# Importing Managers and util functions from duckobot's own library
from Library.Managers.LanguageManager import Language
from Library.Managers.DBManager import DBManager
from Library.Util.GetConfigData import getData
from Library.Util.EmbedGenerator import embf
from Library.Util.GenerateID import generateID
#
APPROVED_EMOJI = f"<:approved:{getData('emotes', 'approved')}>" # Emote One
REJECTED_EMOJI = f"<:rejected:{getData('emotes', 'rejected')}>" # Emote Two
db = DBManager
usersDB = DBManager.UsersManager

rawData = DBManager.getRawData()


class GetSpotifyData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def getspotifydata(self, ctx, *args):
        embed = discord.Embed(description = f"""Artist: {ctx.author.activities[0].artist}\nNume: {ctx.author.activities[0].title}\nAlbum: {ctx.author.activities[0].album}\nCand o inceput sa asculte: {ctx.author.activities[0].created_at}""")
    
        #await ctx.send(f"""{ctx.author.activities[0].artist}\n{ctx.author.activities[0].album}\n{ctx.author.activities[0].created_at}""") 
        await ctx.send(embed = embed)                 
        pass

        
            
 

def setup(bot):
    bot.add_cog(GetSpotifyData(bot))

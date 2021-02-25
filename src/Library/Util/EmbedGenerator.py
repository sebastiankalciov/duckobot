import discord
from discord.ext import commands
import glob


def embf(text, color = 0xd14242):
    """## Embed Generator for duckobot
    Generates an embed object.

    Parameters
    ----------

    text:  :string:
            The text that will be displayed in description.

    color:  :color:
            The color that the embed will have.

    Returns
    -------
    
    Embed object.

    """
    embed = discord.Embed(description = text, color = color)
    return embed
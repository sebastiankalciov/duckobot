import glob # Importing glob to get the commands from folders
import discord # Importing discord library to send messages to user.

async def ReloadCommand(self, ctx, bot, dir_name, success_msg, unsuccess_msg):
        
    """
    ## Reload command of duckobot

    Reloads a command.

    Parameters
    ----------

        self: :class: :parameter:
              Parameter.

        ctx: :class: :variable:
             Parameter.

        bot: :class: :variable:
             Client.

        dir_name: :string:
                  The folder where commands are.  

        success_msg: :string:
                     The message that will be sent if the command was reloaded successfully.

        unsuccess_msg: :string:
                       The message that will be sent if the command was reloaded unsuccessfully.
    
    """

    all_commands = glob.glob(f'./{dir_name}/**/*.py') # A list with all .py files in dir_name.

    try:

        for file in all_commands: # For every file in the list
            if file[2:].replace('\\', '.')[:-3].split(".")[2].lower() == ctx.lower(): # If the current file's name is as the same as required file

                                                        
                bot.unload_extension(file[2:].replace('\\', '.')[:-3]) # Unload the command
                bot.load_extension(file[2:].replace('\\', '.')[:-3]) # Load the command

                embed = discord.Embed(description = success_msg, color=0x5fab38) # Create an embed
                return await self.send(embed = embed) # Send the embed.

    except Exception as e: # If there is a problem with a file
        return await self.send(embed = unsuccess_msg, color=0xd14242) # Break the operation and return a message.


# Docs #

        # << file[2:].replace('\\', '.')[:-3].split(".")[2].lower() >> --> File's name lower cased. (eg. help)
        # << ctx.lower() >> --> Input lower cased. (eg. help)

# Docs #




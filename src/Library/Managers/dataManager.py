# With this manager we send data from bot to a file, and from that file we send to the website.

import json

data = json.load(open('../data.json', "r")) # Loading the data from <data.json>

class DataManager():

    """ Data manager for duckobot-site API """

    def setData(client):

        """ Update <data.json> with real-time informations. """

        with open('../data.json', "r+") as f:
            
            dataFile = json.load(f)
            dataFile["name"] = str(client.user.name)
            dataFile["tag"] = str(client.user.discriminator)
            dataFile["guildSize"] = len(client.guilds)
            dataFile["botAvatar"] = f"https://cdn.discordapp.com/avatars/{client.user.id}/{client.user.avatar}"
            f.seek(0)
            f.write(json.dumps(dataFile, indent = 4))

    def getRawData():

        """Get raw data from <data.json>"""
        data = json.load(open('../data.json', "r"))
        return data

    def modifyData(option, value):

        """ Change the value of an option from <data.json> """
        pass





# With this class we send data from bot to a file, and from that file we send to the website.
# facem ducktheduck/duckobot in github pages si in main folder facem un fisier data.json
# apoi in ducktheduck/duckobot-site in fisierele py... luam din ducktheduck.github.io/duckobot/data.json datele
# pentru ca in duckobot modificam datele de fiecare data cand rulam botu iar in site luam date noi fiindca is actualizate
import json

data = json.load(open('../data.json', "r"))

class DataManager():
    """ Data manager for duckobot-site API """

    def setData(client):
        with open('../data.json', "r+") as f:
            dataFile = json.load(f)
            dataFile["name"] = str(client.user.name)
            dataFile["tag"] = str(client.user.discriminator)
            dataFile["guildSize"] = len(client.guilds)
            dataFile["botAvatar"] = f"https://cdn.discordapp.com/avatars/{client.user.id}/{client.user.avatar}"
            f.seek(0)
            f.write(json.dumps(dataFile, indent = 4))

    def getRawData():
        data = json.load(open('../data.json', "r"))
        return data
    def modifyData(option):
        pass





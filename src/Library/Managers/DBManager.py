
import asyncio
import asyncpg
import json
data = json.load(open(f'./Library/Database/db.json', "r", encoding="utf-8", errors="replace"))

class DBManager ():
    """## DataBase manager of duckobot"""

    def getRawData():
        return data


    async def addData(): # Add a new *table*

        pass

    async def getData(): # Get a whole table.

        pass


    class UsersManager():
        """
        ## DataBase Manager of `duckobot's` users db.
        """

        def addUser(param1, param2, param3): # Add a new user in table.
            pass

        def getData(user, option): # Get data of an existing user.
            pass

        def setData(user, option, param): # Update data with real time information or with specifiec info.
            pass







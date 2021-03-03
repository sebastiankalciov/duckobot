
import asyncio
import asyncpg
import json
data = json.load(open(f'./Library/Database/db.json', "r", encoding="utf-8", errors="replace"))

class DBManager ():
    """## DataBase manager of duckobot"""

    def getRawData():
        """## Get raw data from <db.json>"""
        return data


    def addData(): # Add a new *table*
        """
        ## Add a new table to <db.json>
        """

        pass

    def getData(table): # Get a whole table.
        """
        ## Get a whole table of data from <db.json>
        """

        if data.get(table) == None:
            return "None"
        return data.get(table)


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







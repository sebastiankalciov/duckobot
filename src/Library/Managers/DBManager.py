
import asyncio
import asyncpg

class DBManager ():
    """ DataBase manager for duckobot"""
    async def createDB():

        credentials = {"user": "USERNAME", "duckobot-id": "ID", "database": "DATABASE", "host": "127.0.0.1"}
        db = await asyncpg.create_pool(**credentials)

        await db.execute("CREATE TABLE IF NOT EXISTS users(id bigint PRIMARY KEY, data text);")

        print(db)

    async def getData():

        pass

    def setData():
        pass

loop = asyncio.get_event_loop()
loop.run_until_complete(DBManager().createDB())
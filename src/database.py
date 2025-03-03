from prisma import Prisma

db = Prisma()


async def connect_db():
    await db.connect()


async def disconect_db():
    await db.disconnect()

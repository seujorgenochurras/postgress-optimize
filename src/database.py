from prisma import Prisma
import prisma

db = Prisma()


async def connect_db():
    await db.connect()
    prisma.register(db)


async def disconect_db():
    await db.disconnect()

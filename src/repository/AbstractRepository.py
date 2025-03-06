from abc import ABC
from prisma import Prisma


class AbstractRepository(ABC):
    def __init__(self, prisma: Prisma):
        self._db = prisma

from kink import di
from prisma import Prisma
from src.database import db


def bootstrap_di():
    di[Prisma] = db

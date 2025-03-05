from typing import Optional
from src.injector import Injector
from src.repository.AbstractRepository import AbstractRepository
from prisma.types import UserCreateInput
from prisma.models import User


@Injector(alias=AbstractRepository)
class UserRepository(AbstractRepository):
    async def find_all(self):
        return await self._db.user.find_many(include={"cards": True})

    async def create(self, user: UserCreateInput):
        return await self._db.user.create(data=user)

    async def find_by_email(self, email: str) -> Optional[User]:
        return await self._db.user.find_unique(where={"email": email})

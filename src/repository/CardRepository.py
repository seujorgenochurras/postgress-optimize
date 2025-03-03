from src.injector import Injector
from src.repository.AbstractRepository import AbstractRepository


@Injector(alias=AbstractRepository)
class CardRepository(AbstractRepository):
    async def find_by_user(self, user_id: int):
        return await self._db.card.find_many(where={"userId": user_id})

    async def find_active_by_user(self, user_id: int):
        return await self._db.card.find_many(where={"userId": user_id, "active": True})

    async def create(self, user_id: int, title: str):
        return await self._db.card.create(
            data={"title": title, "userId": user_id, "active": True}
        )

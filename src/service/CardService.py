from src.injector import Injector
from src.repository.CardRepository import CardRepository


@Injector()
class CardService:
    def __init__(self, card_repository: CardRepository):
        self.card_repository = card_repository

    async def find_active_by_user(self, user_id: int):
        return await self.card_repository.find_active_by_user(user_id)

    async def create(self, user_id: int, title: str):
        return await self.card_repository.create(user_id, title)

from src.injector import Injector
from src.repository.UserRepository import UserRepository
from src.dto.UserDto import CreateUserDto
from src.service.CardService import CardService


@Injector()
class UserService:
    def __init__(self, user_repository: UserRepository, card_service: CardService):
        self.user_repository = user_repository
        self.card_service = card_service

    async def find_all(self):
        return await self.user_repository.find_all()

    async def create(self, create_user_dto: CreateUserDto):
        persisted_user = await self.find_by_email(create_user_dto.email)

        if persisted_user:
            return None

        return await self.user_repository.create(create_user_dto)

    async def find_by_email(self, email: str):
        return await self.user_repository.find_by_email(email=email)

    async def find_tasks(self, user_id: int):
        return await self.card_service.find_active_by_user(user_id)
        # tasks = await self.task_service.find_by_card_and_status()

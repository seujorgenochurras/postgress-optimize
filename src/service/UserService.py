from src.injector import Injector
from src.repository import TaskRepository
from src.repository.UserRepository import UserRepository
from src.dto.UserDto import CreateUserDto
from src.service.CardService import CardService
from prisma.enums import TaskStatus

from src.service.TaskService import TaskService


@Injector()
class UserService:
    def __init__(
        self,
        user_repository: UserRepository,
        card_service: CardService,
        task_service: TaskService,
        task_repository : TaskRepository
    ):
        self.user_repository = user_repository
        self.card_service = card_service
        self.task_service = task_service
        self.task_repository = task_repository

    async def find_all(self):
        return await self.user_repository.find_all()

    async def create(self, create_user_dto: CreateUserDto):
        persisted_user = await self.find_by_email(create_user_dto.email)

        if persisted_user:
            return None

        return await self.user_repository.create(
            {"email": create_user_dto.email, "name": create_user_dto.name}
        )

    async def find_by_email(self, email: str):
        return await self.user_repository.find_by_email(email=email)

    async def find_tasks(self, user_id: int, status: TaskStatus):
        return await self.task_service.find_status_by_user(user_id, status)
    
    async def find_tasks_slow(self, user_id: int, status: TaskStatus):
        return await self.task_repository.find_status_by_user_slow(user_id, status)
    
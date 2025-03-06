from src.dto.CreateTaskDto import CreateTaskDto
from src.injector import Injector
from src.repository.TaskRepository import TaskRepository
from prisma.enums import TaskStatus


@Injector()
class TaskService:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    async def create(self, task_dto: CreateTaskDto):
        return await self.task_repository.create(
            task={
                "cardId": task_dto.card_id,
                "description": task_dto.description,
            }
        )

    async def find_status_by_user(self, user_id: int, status: TaskStatus):
        return await self.task_repository.find_status_by_user(user_id, status)

from fastapi import APIRouter

from src.dto.CreateTaskDto import CreateTaskDto
from src.injector import Resolve
from src.service.TaskService import TaskService


router = APIRouter(prefix="/task", tags=["task"])


task_service = Resolve(TaskService)


@router.post("/")
async def create_task(task_dto: CreateTaskDto):
    return await task_service().create(task_dto)

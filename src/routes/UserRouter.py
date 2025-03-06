from fastapi import APIRouter
from src.dto.UserDto import CreateUserDto
from src.injector import Resolve
from src.service.UserService import UserService
from prisma.partials import UserSafe
from prisma.enums import TaskStatus

router = APIRouter(prefix="/user", tags=["user"])

user_service = Resolve(UserService)


@router.get("/", response_model=list[UserSafe])
async def find_all_users():
    return await user_service().find_all()


@router.post("/")
async def create_user(user: CreateUserDto):
    return await user_service().create(user)


@router.get("/{user_id}/task")
async def get_pending_tasks(user_id: int):
    return await user_service().find_tasks(user_id, status=TaskStatus.TODO)

@router.get("/{user_id}/task/slow")
async def get_pending_tasks_slow(user_id: int):
    return await user_service().find_tasks_slow(user_id, status=TaskStatus.TODO)

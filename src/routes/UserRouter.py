from fastapi import APIRouter
from src.dto.UserDto import CreateUserDto
from src.injector import Resolve
from src.service.UserService import UserService
from prisma.partials import UserSafe
router = APIRouter()

user_service = Resolve(UserService)


@router.get("/user", response_model=list[UserSafe])
async def find_all_users():
    return await user_service().find_all()


@router.post("/user")
async def create_user(user: CreateUserDto):
    return await user_service().create(user)

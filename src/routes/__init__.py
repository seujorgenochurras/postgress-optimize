from fastapi import APIRouter

from src.routes import CardRouter, PingRouter, UserRouter

main_router = APIRouter(prefix="/api")

main_router.include_router(UserRouter.router)
main_router.include_router(PingRouter.router)
main_router.include_router(CardRouter.router)
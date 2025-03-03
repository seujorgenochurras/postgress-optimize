from src.bootstrap import bootstrap_di
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.routes import main_router
from src.database import connect_db, disconect_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    bootstrap_di()

    yield
    await disconect_db()


app = FastAPI(lifespan=lifespan)

app.include_router(router=main_router)

from src.bootstrap import bootstrap_di
from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.routes import main_router
from src.database import connect_db, disconect_db
from scalar_fastapi import get_scalar_api_reference  # type: ignore


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_db()
    bootstrap_di()

    yield
    await disconect_db()


app = FastAPI(lifespan=lifespan)


# TODO: get this shit out of here
@app.get("/api/scalar", include_in_schema=False)
def scalar():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title=app.title) # type: ignore


app.include_router(router=main_router)

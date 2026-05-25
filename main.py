from database import create_tables, delete_tables
from fastapi import FastAPI

from contextlib import asynccontextmanager
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("App is cleaned up")
    await create_tables()
    print("App is started up")
    yield
    print("App is shut down")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

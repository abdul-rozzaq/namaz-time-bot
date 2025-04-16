from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.services.bot import BotService
from src.config.settings import init_db, close_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await BotService.load_application()
    await init_db()
    yield
    await close_db()

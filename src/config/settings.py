from pathlib import Path
from environs import Env
from tortoise import Tortoise

import os

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = env.bool("DEBUG", default=False)

BOT_TOKEN = env.str("BOT_TOKEN", default=None)
WEBHOOK_URL = env.str("WEBHOOK_URL", default=None)
REGION_BUTTONS_COLUMN = 2


TORTOISE_CONFIG = {
    "connections": {
        "default": "sqlite://db.sqlite3",
    },
    "apps": {
        "models": {
            "models": ["src.models"],
            "default_connection": "default",
        }
    },
}


async def init_db():
    await Tortoise.init(config=TORTOISE_CONFIG)
    await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()


assert BOT_TOKEN is not None, "BOT_TOKEN is required"
assert WEBHOOK_URL is not None, "WEBHOOK_URL is required"

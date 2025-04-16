from fastapi import APIRouter, Request

from src.services.bot import BotService

router = APIRouter(tags=["WEBHook"])

service = BotService()


@router.post("/")
async def webhook(request: Request):
    request_body = await request.json()

    await service.process_update(request_body)

    return {"status": "ok"}

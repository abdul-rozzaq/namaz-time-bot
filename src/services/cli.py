from telegram import Bot
from src.config.settings import BOT_TOKEN, WEBHOOK_URL
import asyncio


class CLIService:
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)

    def set_webhook(self):
        async def wrapper():
            url = WEBHOOK_URL + "/telegram-webhook/"
            print("URL", url)

            try:
                status = await self.bot.set_webhook(url)

                return status, "Webhook muvaffaqqiyatli o'rnatildi"
            except Exception as e:
                return False, str(e)

        return asyncio.run(wrapper())

    def delete_webhook(self):
        async def wrapper():
            try:
                status = await self.bot.delete_webhook()

                return status, "Webhook muvaffaqqiyatli o'chirildi"
            except Exception as e:
                return False, str(e)

        return asyncio.run(wrapper())

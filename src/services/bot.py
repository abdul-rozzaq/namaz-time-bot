from telegram import Update
from telegram.ext import Application, CommandHandler, ConversationHandler, MessageHandler, filters

from src.config.settings import BOT_TOKEN
from src.handlers import start, set_region, todays_pray_time


class BotService:
    application: Application

    async def process_update(self, jsondata):
        update = Update.de_json(jsondata, bot=self.application.bot)

        await self.application.process_update(update)

    @classmethod
    async def load_application(cls):
        application = Application.builder().token(BOT_TOKEN).build()

        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.Regex(r"^Bugungi namoz vaqtlari$"), todays_pray_time))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, set_region))

        await application.initialize()
        await application.start()

        cls.application = application

        print("✅ Telegram bot started")

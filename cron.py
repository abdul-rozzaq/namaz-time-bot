import asyncio
from tortoise import Tortoise
from telegram import Bot
from src.services.pray_time_service import PrayTimeService
from src.config.settings import BOT_TOKEN, init_db


async def send_prayer_times():
    await init_db()

    from src.models import TelegramUser

    bot = Bot(token=BOT_TOKEN)

    try:
        users = await TelegramUser.all()

        for user in users:

            if user.region_id > 0:
                pray_time_service = PrayTimeService(user.region_id)
                region_name, times = pray_time_service.todays_pray_time()

                if region_name is not None:
                    message = f"""📍 Hudud: {region_name}\n\n📅 Sana: {times['kun']}, {times['hafta_kuni']}\n🌅 Saharlik: {times['saharlik']}\n☀️ Quyosh: {times['quyosh']}\n🕌 Peshin: {times['peshin']}\n🕌 Asr: {times['asr']}\n🌇 Iftorlik: {times['iftorlik']}\n🌌 Xufton: {times['xufton']}"""

                    await bot.send_message(chat_id=user.telegram_id, text=message)

    finally:
        await Tortoise.close_connections()


if __name__ == "__main__":
    asyncio.run(send_prayer_times())

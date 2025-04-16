from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from datetime import datetime
from src.services.pray_time_service import PrayTimeService
from src.models import TelegramUser
from src.config.settings import REGION_BUTTONS_COLUMN

import json


with open("data/regions.json", "r", encoding="utf-8") as file:
    REGIONS = json.loads(file.read())
    REGIONS_KEYS = sorted(list(REGIONS.keys()))


start_buttons = ReplyKeyboardMarkup(
    [REGIONS_KEYS[i : i + REGION_BUTTONS_COLUMN] for i in range(0, len(REGIONS_KEYS), REGION_BUTTONS_COLUMN)],
    one_time_keyboard=True,
    resize_keyboard=True,
)
todays_pray_time_buttons = ReplyKeyboardMarkup(
    [["Bugungi namoz vaqtlari"]],
    one_time_keyboard=True,
    resize_keyboard=True,
)


async def start(update: Update, context: CallbackContext):
    user = update.effective_user

    await update.message.reply_text(
        f"Assalomu alaykum {user.first_name}\n\nHududingizni tanlang:",
        reply_markup=start_buttons,
    )

    await TelegramUser.get_or_create(telegram_id=user.id, defaults={"telegram_id": user.id, "region_id": 0})


async def set_region(update: Update, context: CallbackContext):
    region_name = update.message.text

    await TelegramUser.filter(telegram_id=update.effective_user.id).update(region_id=REGIONS[region_name])

    await update.message.reply_text(f"✅ Sizning Hududingiz: {region_name}", reply_markup=todays_pray_time_buttons)


async def todays_pray_time(update: Update, context: CallbackContext):
    user = await TelegramUser.get_or_none(telegram_id=update.effective_user.id)

    if user is not None:
        region_id = user.region_id

        if region_id > 0:
            pray_time_service = PrayTimeService(region_id)

            region_name, times = pray_time_service.todays_pray_time()
            message = f"""📍 Hudud: {region_name}\n\n📅 Sana: {times['kun']}, {times['hafta_kuni']}\n🌅 Saharlik: {times['saharlik']}\n☀️ Quyosh: {times['quyosh']}\n🕌 Peshin: {times['peshin']}\n🕌 Asr: {times['asr']}\n🌇 Iftorlik: {times['iftorlik']}\n🌌 Xufton: {times['xufton']}"""

            await update.message.reply_text(message, reply_markup=todays_pray_time_buttons)

            return

    await TelegramUser.get_or_create(telegram_id=user.id, defaults={"telegram_id": user.id, "region_id": 0})
    await update.message.reply_text("Hududingizni tanlang", reply_markup=start_buttons)

    return

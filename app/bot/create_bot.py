from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.core.config import setting_conn

bot = Bot(
    token=setting_conn.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()


async def start_bot():
    try:
        await bot.send_message(setting_conn.ADMIN_ID, f"Я запущен🥳.")
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(setting_conn.ADMIN_ID, "Бот остановлен. За что?😔")
    except:
        pass

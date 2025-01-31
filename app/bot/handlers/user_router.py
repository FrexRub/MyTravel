import logging
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.core.dao import UserDAO
from app.bot.keyboards.kbs import app_keyboard
from app.bot.utils.utils import greet_user, get_about_us_text
from app.core.config import configure_logging

user_router = Router()


configure_logging(logging.INFO)
logger = logging.getLogger(__name__)


@user_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """
    Обрабатывает команду /start.
    """
    user = await UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    logger.info("Run command /start for user %s" % user)
    if not user:
        await UserDAO.add(
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            username=message.from_user.username,
        )

    await greet_user(message, is_new_user=not user)


@user_router.message(F.text == "🔙 Назад")
async def cmd_back_home(message: Message) -> None:
    """
    Обрабатывает нажатие кнопки "Назад".
    """
    await greet_user(message, is_new_user=False)


@user_router.message(F.text == "ℹ️ О боте")
async def about_us(message: Message):
    kb = app_keyboard(
        user_id=message.from_user.id, first_name=message.from_user.first_name
    )
    await message.answer(get_about_us_text(), reply_markup=kb)

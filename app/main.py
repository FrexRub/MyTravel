import logging

import uvicorn
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from app.core.config import configure_logging
from your_bot_module import bot, dp, settings  # Импортируем необходимые компоненты бота

configure_logging(logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Код, выполняющийся при запуске приложения
    webhook_url = settings.get_webhook_url()  # Получаем URL вебхука
    await bot.set_webhook(
        url=webhook_url,
        allowed_updates=dp.resolve_used_update_types(),
        drop_pending_updates=True
    )
    logger.info(f"Webhook set to {webhook_url}")
    yield  # Приложение работает
    # Код, выполняющийся при завершении работы приложения
    await bot.delete_webhook()
    logger.info("Webhook removed")


# Инициализация FastAPI с методом жизненного цикла
app = FastAPI(lifespan=lifespan)


# Маршрут для обработки вебхуков
@app.post("/webhook")
async def webhook(request: Request) -> None:
    logger.info("Received webhook request")
    update = await request.json()  # Получаем данные из запроса
    # Обрабатываем обновление через диспетчер (dp) и передаем в бот
    await dp.feed_update(bot, update)
    logger.info("Update processed")


if __name__ == "__main__":
    uvicorn.run("main:app")

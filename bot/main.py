import asyncio
import logging
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'bot'))

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import bot_config
from database import init_db
from commands_setup import setup_bot_commands
from handlers.start import router as start_router
from handlers.chat_management import router as chat_router
from handlers.command_management import router as command_router
from handlers.custom_commands import router as custom_router

async def main():
    # Инициализация базы данных
    init_db()
    
    # Настройка бота
    bot = Bot(token=bot_config.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    
    # Устанавливаем команды меню
    await setup_bot_commands(bot)
    
    # Регистрация роутеров
    dp.include_router(start_router)
    dp.include_router(chat_router)
    dp.include_router(command_router)
    dp.include_router(custom_router)
    
    # Запуск бота
    await bot.delete_webhook(drop_pending_updates=True)
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

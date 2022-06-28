from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.config.config import TOKEN
from aiogram import Bot

class CreateBot:
    '''Создание бота'''
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
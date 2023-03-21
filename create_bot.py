from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from environs import Env
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

env = Env()
env.read_env()

storage=MemoryStorage()

BOT_TOKEN = env.str("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)
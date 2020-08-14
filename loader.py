from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiohttp import BasicAuth
import os

from data import config

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
PROXY = str(os.getenv("PROXY"))
LOGIN = str(os.getenv("LOGIN"))
PASSWORD = str(os.getenv("PASSWORD"))


#if proxy needs:
# bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML, proxy=config.PROXY, proxy_auth=BasicAuth(config.LOGIN, config.PASSWORD))

bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

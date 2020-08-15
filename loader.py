from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiohttp import BasicAuth
from data import config

#if proxy needs:
# bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML, proxy=config.PROXY, proxy_auth=BasicAuth(config.LOGIN, config.PASSWORD))

bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

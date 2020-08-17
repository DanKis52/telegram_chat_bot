import requests
import re
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('joke'))
async def send_joke(message: types.Message):
    response = requests.get('https://ultragenerator.com/anekdotov/handler.php').text
    text = response.replace('<br />', '')
    p = re.compile(r'<.*?>')
    no_tag_text = p.sub('', text)
    await message.answer(text=no_tag_text)

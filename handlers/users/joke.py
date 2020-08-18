import logging

import requests
import re
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('joke'))
async def send_joke(message: types.Message):
    logging.info(
        f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    response = requests.get('https://ultragenerator.com/anekdotov/handler.php').text
    del_tags = re.compile(r'<.*?>')
    no_tag_text = del_tags.sub('', response)
    await message.answer(text=no_tag_text)

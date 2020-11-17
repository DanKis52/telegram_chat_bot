import logging

import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('meme'))
async def send_cat(message: types.Message):
    logging.info(
        f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    response = requests.get('https://meme-api.herokuapp.com/gimme/dankmemes').json()
    url = response['url']
    await message.answer_photo(photo=url)
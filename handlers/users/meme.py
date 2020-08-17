import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('meme'))
async def send_cat(message: types.Message):
    response = requests.get('https://meme-api.herokuapp.com/gimme').json()
    url = response['url']
    await message.answer_photo(photo=url)
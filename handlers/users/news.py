import json
import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from data import config
from loader import dp
import requests

from utils.misc import rate_limit


@rate_limit(10800, 'news')
@dp.message_handler(Command('news'))
async def send_news(message: types.Message):
    logging.info(
        f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    await message.answer(text="Данную команду можно использовать только раз в три часа")
    key = config.MS_KEY
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/news/search"
    headers = {"Ocp-Apim-Subscription-Key": key}
    params = {"q": "Нижний Новгород"}
    response = requests.get(search_url, headers=headers, params=params)
    search_results = response.json()
    values = search_results['value']
    out = []
    for value in values:
        out.append(value['name']+' <a href="'+value['url']+'">Читать</a>\n\n')
    outsting = ''.join(out)
    await message.answer(text=f"{outsting}")


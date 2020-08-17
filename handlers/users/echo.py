import requests
from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    response = (requests.get('http://free-generator.ru/generator.php?action=quote&src=0')).json()
    text = response['quote']['quote']
    await message.answer(text=f"{text}\n\n"
                              f"Напиши /help и узнай, что я могу")

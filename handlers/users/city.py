import logging
from aiogram import types
from aiogram.dispatcher.filters import Command
from data.cities_list import get_city_list
from states import City
from aiogram.dispatcher import FSMContext
from loader import dp


@dp.message_handler(Command('city'))
async def start_game(message: types.Message):
    logging.info(
        f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    if message.chat.type == 'private':
        await message.answer(text="Игра в города, 20 ответов, для старта напиши город, для выхода напиши /exit")
        await City.first()
    else:
        await message.answer(text="Доступно только для приватных чатов!")

@dp.message_handler(state=City.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        await state.finish()
    else:
        cities = get_city_list()
        if message.text.title() in cities:
            await message.answer(text="Ты проебал в любом случае")
        else:
            await message.answer(text="Я не знаю такого города, введи другой")




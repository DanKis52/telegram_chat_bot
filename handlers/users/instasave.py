import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
import requests
from data import config
from loader import dp, bot
from states import Instastates


@dp.message_handler(Command("instasave"))
async def ask_link(message: types.Message):
    logging.info(
        f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    await message.answer(text="Введи ссылку на фото, для выхода напиши /exit")
    await Instastates.first()

@dp.message_handler(state=Instastates.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    if message.text.lower() == "/exit" or message.text.lower() == "/exit@don_mafioznik_bot":
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} вышел в меню")
        await state.finish()
        await message.answer(text="Ты вышел в меню")
    else:
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел ссылку {message.text}")
        base_url = message.text.split('/')
        try:
            if base_url[2] in ["www.instagram.com", "instagram.com"]:
                complete_url = 'https://www.instagram.com/p/'+base_url[4]+'/?__a=1'
                response = requests.get(complete_url).json()
                jpg_link = response['graphql']['shortcode_media']['display_url']
                await message.answer_photo(photo=jpg_link)
                await message.answer(text='Отправь еще одну ссылку или введи /exit для выхода в меню')
            else:
                await message.answer(text="Ссылка введена неверно")
        except:
            await message.answer(text="Это по твоему ссылка?")


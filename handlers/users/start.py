import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(
        f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    await message.answer(f'Привет, {message.from_user.full_name}!\n'
                         f'Напиши мне что-нибудь, и я тебе что-нибудь отвечу\n'
                         f'Для просмотра доступных команд напиши /help или нажми на / внизу')

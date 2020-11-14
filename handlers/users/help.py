import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    logging.info(f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    await message.answer(text=f"Список доступных тебе команд:\n"
                              f"/instasave - скачать фото из Instagram по ссылке\n"
                              f"/city - игра в города России\n"
                              f"/meme - получить пендосский мем\n"
                              f"/joke - несмешные шутки\n"
                              f"/weather - прогноз погоды\n"
                              f"/covid - статистика по коронавирусу\n"
                              f"/news - новости в Нижнем Новгороде")

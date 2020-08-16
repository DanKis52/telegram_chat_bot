from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(text=f"Список доступных тебе команд:\n"
                              f"/weather - прогноз погоды\n"
                              f"/covid - статистика по коронавирусу")

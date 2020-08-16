from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await message.answer(text=f"Братанчик, я бот, че ты пытаешься мне сказать? {message.text.capitalize()}? Лучше напиши мне /help и узнай, что я могу")

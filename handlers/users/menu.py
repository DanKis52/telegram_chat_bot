from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Choose one item from menu below:", reply_markup=menu)

@dp.message_handler(Text(equals=["Item 1","Item 2"]))
async def get_item(message: types.Message):
    await message.answer(f"Your сhoice: {message.text}", reply_markup=ReplyKeyboardRemove())
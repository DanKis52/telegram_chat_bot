import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.buy_inline import choice, beer_keyboard
from keyboards.inline.callback_datas import buy_callback
from loader import dp


@dp.message_handler(Command("purchase"))
async def show_items(message: types.Message):
    await message.answer(text="There's what you can buy:", reply_markup=choice)


@dp.callback_query_handler(buy_callback.filter(item_name="Beer"))
async def buying_beer(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Your choice is Beer, quantity is {quantity}",reply_markup=beer_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="Cola"))
async def buying_cola(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    logging.info(f"callback_data dict = {callback_data}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Your choice is Cola, quantity is {quantity}")


@dp.callback_query_handler(text="cancel")
async def cancel(call: CallbackQuery):
    await call.answer("You closed the menu", show_alert=True)
    await call.message.edit_reply_markup()
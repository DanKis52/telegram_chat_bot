from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Test started:\n"
                         "Question 1:\n"
                         "Type something...")
    await Test.first()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(answer1 = answer)
    await message.answer("Question 2:\n"
                         "Type something more...")
    await Test.next()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = message.text

    await message.answer('Thanks for response :*')
    await message.answer(f"Response 1: {answer1}")
    await message.answer(f"Response 2: {answer2}")

    await state.finish()

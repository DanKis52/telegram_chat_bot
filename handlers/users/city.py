import logging
import random

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
        await message.answer(
            text="Игра в города России, вряд ли ты победишь этого бота, для старта напиши город, для выхода напиши /exit\n\n"
                 "Йошкар-Ола в игре не участвует, других городов на 'Й' нет!")
        await City.first()
    else:
        await message.answer(text="Доступно только для приватных чатов!")


@dp.message_handler(state=City.Q1)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        cities = get_city_list()
        if message.text.title() in cities:
            cities.remove(message.text.title())
            last_letter = message.text.upper()[-1]
            last_letter_2 = message.text.upper()[-2]
            rand_answer = []
            for city in cities:
                if city.startswith(last_letter):
                    rand_answer.append(city)
            if len(rand_answer) == 0:
                for city in cities:
                    if city.startswith(last_letter_2):
                        rand_answer.append(city)
            answer_city = rand_answer[random.randint(0, len(rand_answer))]
            cities.remove(answer_city)
            await message.answer(text=answer_city)
            answer_last_letter = answer_city[-1]
            if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                answer_last_letter = answer_city[-2]
            if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                answer_last_letter = answer_city[-3]
            await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
            await City.next()
        else:
            await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")


@dp.message_handler(state=City.Q2)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q3)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q4)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q5)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q6)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q7)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q8)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q9)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q10)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text="Тебе еще не надоело?")
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q11)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text="Остановись")
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q12)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text="Я серьезно, хватит")
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q13)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, в конце игры пасхалка")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                cities.remove(message.text.title())
                last_letter = message.text.upper()[-1]
                last_letter_2 = message.text.upper()[-2]
                rand_answer = []
                for city in cities:
                    if city.startswith(last_letter):
                        rand_answer.append(city)
                if len(rand_answer) == 0:
                    for city in cities:
                        if city.startswith(last_letter_2):
                            rand_answer.append(city)
                answer_city = rand_answer[random.randint(0, len(rand_answer))]
                cities.remove(answer_city)
                await message.answer(text="Последнее предупреждение")
                await message.answer(text=answer_city)
                answer_last_letter = answer_city[-1]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-2]
                if answer_last_letter == 'ь' or answer_last_letter == 'ъ' or answer_last_letter == 'ы' or answer_last_letter == 'й':
                    answer_last_letter = answer_city[-3]
                await state.update_data(upd_cities=cities, answer_last_letter=answer_last_letter)
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел город {message.text}, ответ бота {answer_city}")
                await City.next()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")


@dp.message_handler(state=City.Q14)
async def bot_answer_city(message: types.Message, state: FSMContext):
    if message.text.lower() == '/exit':
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        await message.answer(text="Зря ты вышел, ты почти победил")
        await state.finish()
    else:
        data = await state.get_data()
        cities = data.get("upd_cities")
        last_letter = data.get("answer_last_letter")
        if last_letter.upper() == message.text.title()[0]:
            if message.text.title() in cities:
                logging.info(
                    f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text} и выиграл у бота в города")
                await message.answer(text="Я тебя предупреждал")
                await message.answer(text="/exit")
                await message.answer(text="Я вышел в меню за тебя, кусок мяса")
                await state.finish()
            else:
                await message.answer(text="Я не знаю такого города или он уже был введен, введи другой")
        else:
            await message.answer(text="Кого ты пытаешься обмануть?")

import logging
from data import config
from time import sleep
from urllib.parse import urlsplit
from aiogram.dispatcher import FSMContext
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Insta


@dp.message_handler(Command("instasave"))
async def print_weather(message: types.Message):
    logging.info(
        f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    await message.answer(text="Введи ссылку на фото, для выхода напиши /exit")
    await Insta.first()


@dp.message_handler(state=Insta.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    if message.text.lower() == "/exit" or message.text.lower() == "/exit@don_mafioznik_bot":
        logging.info(f"{message.from_user.first_name, message.from_user.username, message.from_user.id} вышел в меню")
        await state.finish()
        await message.answer(text="Ты вышел в меню")
    else:
        logging.info(
            f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
        url = urlsplit(message.text)
        if url.netloc in ["www.instagram.com", "instagram.com"]:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(options=chrome_options, executable_path='/home/ubuntu/stable/Users/kisel/telegram_chat_bot/chromedriver')
            driver.get('https://www.instagram.com')
            logging.info(f"{message.from_user.first_name, message.from_user.username, message.from_user.id} get instagram ok")
            await message.answer(text="Авторизуюсь в Instagram")
            sleep(0.5)
            login_elem = driver.find_element_by_tag_name('form')
            user = login_elem.find_element_by_name('username')
            user.send_keys(config.I_LOGIN)
            password = login_elem.find_element_by_name('password')
            password.send_keys(config.I_PW + '\n')
            logging.info(f"{message.from_user.first_name, message.from_user.username, message.from_user.id} login ok")
            sleep(2)
            await message.answer(text="Открываю ссылку")
            driver.get(message.text)
            logging.info(f"{message.from_user.first_name, message.from_user.username, message.from_user.id} get link ok")
            sleep(2)
            try:
                wrap = driver.find_element_by_xpath('//article[@role="presentation"]')
                img = wrap.find_element_by_xpath('//img[@decoding="auto"]')
                link = img.get_attribute("src")
                logging.info(f"{message.from_user.first_name, message.from_user.username, message.from_user.id} image sended")
                await message.answer_photo(photo=link)
            except:
                logging.info(f"{message.from_user.first_name, message.from_user.username, message.from_user.id} no image")
                await message.answer(text="Не могу найти фото по данной ссылке")
            driver.delete_all_cookies()
            driver.close()
            await state.finish()
        else:
            await message.answer(text="Введи ссылку на фото instagram или напиши /exit для выхода")








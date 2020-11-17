from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging

from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('steam'))
async def send_cat(message: types.Message):
    await message.answer(text="Собираю скидки")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    logging.info(
        f"{message.from_user.first_name, message.from_user.username, message.from_user.id} ввел {message.text}")
    driver = webdriver.Chrome(options=chrome_options,
                              executable_path='/home/ubuntu/stable/Users/kisel/telegram_chat_bot/chromedriver')
    driver.get("https://store.steampowered.com/search/?filter=weeklongdeals&cc=ru")
    list = driver.find_elements_by_class_name("search_result_row")
    out = []
    for apps in list:
        link = apps.get_attribute("href")
        name = apps.find_element_by_class_name("title").text
        price = apps.find_element_by_class_name("discounted").text
        price_list = price.split('\n')
        full_price = price_list[0]
        discount_price = price_list[1]
        out.append(name + ' <strike>'+ full_price+ '</strike> ' + discount_price + ' <a href="' + link + '">Ссылка</a>\n\n')
    outsting = ''.join(out)
    driver.delete_all_cookies()
    driver.close()
    await message.answer(text=f"{outsting}")


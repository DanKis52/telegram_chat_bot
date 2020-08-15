from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
import requests
from data import config
from loader import dp
from states.weather_states import Weather

base_url = "http://api.openweathermap.org/data/2.5/weather?"


@dp.message_handler(Command("weather"))
async def print_weather(message: types.Message):
    await message.answer(text="Input your city, for exit print <b>exit</b>")
    await Weather.first()


@dp.message_handler(state=Weather.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    if message.text.lower() == "exit":
        await state.finish()
    else:
        city = message.text
        complete_url = base_url + "appid=" + config.WEATHER_KEY + "&q=" + city
        response = requests.get(complete_url)
        full_weather_dict = response.json()
        if full_weather_dict['cod'] != "404":
            weather_main = full_weather_dict['main']
            temp = int(weather_main['temp'] - 273)
            feels_like = int(weather_main['feels_like'] - 273)
            humidity = weather_main['humidity']
            pressure = int(weather_main['pressure'] * 0.75006375541921)
            await message.answer(text=f"Weather in {city}:\n"
                                      f"Temperature is {temp} C, feels like {feels_like} C\n"
                                      f"Humidity (влажность) is {humidity} %\n"
                                      f"Pressure is {pressure} mmHg")
        else:
            await message.answer(text="City not found, try again or print <b>exit</b>")

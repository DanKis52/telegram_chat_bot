from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'covid')
@dp.message_handler(Command("covid"))
async def covid_stats(message: types.Message):
    from covid.api import CovId19Data
    api = CovId19Data(force=False)
    res = api.get_history_by_country("russia")

    russia = res['russia']
    history = russia['history']

    current_day = list(history.keys())[-1]
    before_day = list(history.keys())[-2]

    current_info = history[current_day]
    before_info = history[before_day]

    confirmed = current_info['confirmed']
    confirmed_delta = current_info['confirmed'] - before_info['confirmed']

    recovered = current_info['recovered']
    recovered_delta = current_info['recovered'] - before_info['recovered']

    deaths = current_info['deaths']
    deaths_delta = current_info['deaths'] - before_info['deaths']

    await message.answer(text=f"Статистика по коронавирусу в России:\n"
                              f"<i>Информация актуальна на {current_day}</i>\n"
                              f"Заболеваний: <b>{confirmed}</b> ( <b>+{confirmed_delta}</b> за сутки )\n"
                              f"Выздоровлений: <b>{recovered}</b> ( <b>+{recovered_delta}</b> за сутки )\n"
                              f"Смертей: <b>{deaths}</b> ( <b>+{deaths_delta}</b> за сутки )")

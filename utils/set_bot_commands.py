from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("help", "Команды бота"),
        types.BotCommand("weather", "Прогноз погоды"),
        types.BotCommand("covid", "Статистика по коронавирусу")
    ])

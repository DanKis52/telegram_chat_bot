from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("instasave", "Скачать фото из Instagram"),
        types.BotCommand("steam", "Актуальные скидки Steam"),
        types.BotCommand("city", "Игра в города России"),
        types.BotCommand("news", "Новости"),
        types.BotCommand("meme", "Пендосский мем"),
        types.BotCommand("joke", "Несмешные шутки"),
        types.BotCommand("weather", "Прогноз погоды"),
        types.BotCommand("covid", "Статистика по коронавирусу")
    ])

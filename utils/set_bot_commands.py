from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("help", "Команды бота"),
        types.BotCommand("meme", "Пендосский мем"),
        types.BotCommand("joke", "Несмешные шутки"),
        types.BotCommand("weather", "Прогноз погоды"),
        types.BotCommand("covid", "Статистика по коронавирусу")
    ])

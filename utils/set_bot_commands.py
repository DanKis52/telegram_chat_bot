from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Start the bot"),
        types.BotCommand("help", "Info about commands"),
        types.BotCommand("test", "Testing questions"),
        types.BotCommand("menu", "Testing keyboard"),
        types.BotCommand("purchase", "Testing markup keyboard"),
    ])

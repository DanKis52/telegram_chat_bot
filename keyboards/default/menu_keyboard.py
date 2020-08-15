from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Item 1")
        ],
        [
            KeyboardButton(text="Item 2"),
            KeyboardButton(text="Item 3")
        ]
    ],
    resize_keyboard=True
)

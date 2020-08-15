from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="Beer",
                                          callback_data="buy:Beer:1"
                                      ),
                                      InlineKeyboardButton(
                                          text="Cola",
                                          callback_data="buy:Cola:1"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Close",
                                          callback_data="cancel"
                                      )
                                  ]
                              ]
                              )

beer_keyboard = InlineKeyboardMarkup()

BEER_LINK = "https://hoegaarden.com/"

beer_link = InlineKeyboardButton(text="Buy here", url=BEER_LINK)

beer_keyboard.insert(beer_link)



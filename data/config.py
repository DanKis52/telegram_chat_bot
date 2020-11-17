import os
from dotenv import load_dotenv

load_dotenv()

# Get Token
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

# Get Proxy Settings
PROXY = str(os.getenv("PROXY"))
LOGIN = str(os.getenv("LOGIN"))
PASSWORD = str(os.getenv("PASSWORD"))

# Get Weather Token
WEATHER_KEY = str(os.getenv("WEATHER_KEY"))

# Get Microsoft Token
MS_KEY = str(os.getenv("MS_KEY"))

admins = [
    528617712
]

I_LOGIN = str(os.getenv("I_LOGIN"))
I_PW = str(os.getenv("I_PW"))

# Redis DB Settings

# aiogram_redis = {
#     'host': ip,
# }
#
# redis = {
#     'address': (ip, 6379),
#     'encoding': 'utf8'
# }

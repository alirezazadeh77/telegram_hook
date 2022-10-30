from decouple import config

TELEGRAM_TOKEN = config('TELEGRAM_TOKEN', default='')
TELEGRAM_CHAT_ID = config('TELEGRAM_CHAT_ID', default='@server_alert')
import telegram

from app.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def send_message(text):
    telegram_token = TELEGRAM_TOKEN
    telegram_chat_id = TELEGRAM_CHAT_ID
    _bot = telegram.Bot(token=telegram_token)
    _bot.sendMessage(chat_id=chat_id, text=text, parse_mode=telegram.ParseMode.HTML)

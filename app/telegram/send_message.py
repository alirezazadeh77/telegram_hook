import telegram

from app.config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID


def send_message(text):
    telegram_token = TELEGRAM_TOKEN
    telegram_chat_id = TELEGRAM_CHAT_ID
    _bot = telegram.Bot(token=telegram_token)
    str_message = ""
    for key, value in text.items():
        str_message += f'<em><b>{key.replace("_"," ")}:</b></em>\n' \
                       f'{value}\n'

    _bot.sendMessage(chat_id=telegram_chat_id, text=str_message, parse_mode=telegram.ParseMode.HTML)

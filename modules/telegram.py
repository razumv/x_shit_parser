import requests

from settings import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_message_to_user(text: str = ""):
    requests.post(
        f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={text}&parse_mode=Markdown"
    )

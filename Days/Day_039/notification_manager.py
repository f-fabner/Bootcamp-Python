import os
import requests

TELEGRAM_API_URL = "https://api.telegram.org/bot"

class TelegramNotificationManager:
    def __init__(self):#
        self.bot_token = os.environ.get('TELEGRAM_BOT_TOKEN')
        self.chat_id = os.environ.get('TELEGRAM_CHAT_ID')

    def send_message(self, message):
        send_text = f"{TELEGRAM_API_URL}{self.bot_token}/sendMessage?chat_id={self.chat_id}&parse_mode=Markdown&text={message}"
        response = requests.get(send_text)
        return response.json()

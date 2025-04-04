from enum import Enum
import requests


class Condition(Enum):

    MESSAGE = "📩"


class Logger:

    def __init__(self, token, chat_id):
        self._token = token
        self._chat_id = chat_id
        self._url = f"https://api.telegram.org/bot{token}/"

    def log(self, message, condition=None):
        text = message
        if condition is not None:
            text = f"{condition.value} {text}"

        url = self._url + "sendMessage"
        data = {
            "chat_id": self._chat_id,
            "text": text,
            "parse_mode": "HTML"
        }
        resp = requests.post(url=url, json=data)
        resp.raise_for_status()

    def message(self, message):
        self.log(message, Condition.MESSAGE)

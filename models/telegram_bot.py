import re
import telegram
from rules import rules
from settings import settings


class TelegramBot(object):
    def __init__(self, chat_id=None):
        token = settings['token']
        self.chat_id = chat_id
        self.bot = telegram.Bot(token=token)

    def set_chat_id(self, chat_id):
        self.chat_id = chat_id

    def send_message(self, text):
        self.bot.sendMessage(chat_id=self.chat_id, text=text)

    def send_sticker(self, sticker):
        self.bot.sendSticker(chat_id=self.chat_id, sticker=sticker)

    def parse(self, json):
        return telegram.Update.de_json(json, self.bot)

    def check_rules(self, text):
        for rule in rules:
            if re.search(rule, text, re.IGNORECASE):
                (action_type, message) = rules[rule]
                action = self.__getattribute__('send_%s' % action_type)
                action(message)
                return True

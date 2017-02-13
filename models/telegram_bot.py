import re
import random
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

    def send_message(self, text, update=None):
        message_id = None
        if update:
            message_id = update.message.message_id
        self.bot.sendMessage(
            chat_id=self.chat_id,
            text=text,
            reply_to_message_id=message_id,
        )

    def send_sticker(self, text, update):
        self.bot.sendSticker(
            chat_id=self.chat_id,
            sticker=text,
            reply_to_message_id=update.message.message_id,
        )

    def parse(self, json):
        return telegram.Update.de_json(json, self.bot)

    def setWebhook(self):
        return self.bot.setWebhook(settings['hook-url'])

    def check_rules(self, update):
        text = update.message.text
        for rule in rules:
            for regex in rule['rules']:
                if re.search(regex, text, re.IGNORECASE):
                    message = random.choice(rule['actions'])
                    action_type = rule['action_type']
                    action = self.__getattribute__('send_%s' % action_type)
                    action(message, update)
                    return True

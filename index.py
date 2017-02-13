import logging
from models.telegram_bot import TelegramBot
from flask import Flask, request
app = Flask(__name__)


@app.route("/new-message", methods=['POST'])
def new_message():
    if request.method == "POST":
        bot = TelegramBot()
        update = bot.parse(request.get_json(force=True))
        chat_id = update.message.chat.id
        bot.set_chat_id(chat_id)
        text = update.message.text
        bot.check_rules(text)
        return '.'


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(debug=True)

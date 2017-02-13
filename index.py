import logging
from models.telegram_bot import TelegramBot
from flask import Flask, request
app = Flask(__name__)


@app.route("/new-message", methods=['POST'])
def new_message():
    if request.method == "POST":
        bot = TelegramBot()
        update = bot.parse(request.get_json(force=True))
        if not update.message:
            return '.'
        chat_id = update.message.chat.id
        bot.set_chat_id(chat_id)
        
        text = update.message.text
        bot.check_rules(text)
        return '.'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    bot = TelegramBot()
    s = bot.setWebhook()
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(debug=True)

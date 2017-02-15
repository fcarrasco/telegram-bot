import logging
from services.telegram_bot import TelegramBot
from flask import Flask, request, render_template
from settings import settings
app = Flask(__name__)


@app.route("/new-message", methods=['POST'])
def new_message():
    if request.method == "POST":
        bot = TelegramBot()
        update = bot.parse(request.get_json(force=True))
        if not update.message:
            return '.'
        chat_id = update.message.chat.id
        if settings['allowed_chats'] is not None \
           and chat_id not in settings['allowed_chats']:
            print(chat_id)
            return 'chat id not allowed'
        bot.set_chat_id(chat_id)
        debugger = chat_id == settings['debug_chat_id']
        if debugger:
            if update.message.sticker:
                print(update.message.sticker.file_id)
            elif update.message:
                print(update.message)
        bot.check_rules(update)
        return '.'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    bot = TelegramBot()
    s = bot.setWebhook()
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/send_message/', methods=['GET', 'POST'])
def send_message():
    if request.method == "POST":
        message = request.form['message']
        chat_id = request.form['chat_id']
        bot = TelegramBot()
        # 1001050125853
        bot.set_chat_id(chat_id)
        bot.send_message(message)
    return render_template('message.jinja2')


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(debug=True, port=8080)

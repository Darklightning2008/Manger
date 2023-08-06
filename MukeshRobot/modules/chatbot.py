import telegram
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class MyBot:
    def __init__(self, token, api_key):
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.add_handlers()
        openai.api_key = " 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"

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hello! I am your Telegram bot.')

    def get_answer(self, update, context):
        question = ' '.join(context.args)
        response = openai.Completion.create(engine='davinci', prompt=f'Answer the following question: {question}\n', max_tokens=100)
        answer = response.choices[0].text.strip()
        context.bot.send_message(chat_id=update.effective_chat.id, text=answer)

    def add_handlers(self):
        start_handler = CommandHandler('start', self.start)
        answer_handler = CommandHandler('answer', self.get_answer)
        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(answer_handler)

    def run(self):
        self.updater.start_polling()
        self.updater.idle()


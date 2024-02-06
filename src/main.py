import telebot
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)
# bot = AsyncTeleBot(TELEGRAM_TOKEN)


# handle '/start' and '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm a bot. I can help you to\
                 get a list of your favorite books. Just send\
                 me a message and I will send you a list of your\
                favorite books.")


# handler all other messages with conten_type 'text'
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)


# tipe filter in message_handler
# handle all sent document and audio files


# content_types=["text", "sticker", "pinned_message", "photo", "audio"]
@bot.message_handler(content_types=["document", "audio"])
def handle_docs_audio(message):
    bot.reply_to(message, "Sorry, I can't read documents or audio files.")


bot.infinity_polling()

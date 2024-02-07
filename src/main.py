import telebot
from dotenv import load_dotenv
import os
import logging as logger

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

####
# content_types=["text", "sticker", "pinned_message", "photo", "audio"]
####


# handle all sent audio files
@bot.message_handler(content_types=["audio"])
def handle_docs_audio(message):
    bot.reply_to(message, "this is audio.")


# handle all sent photo
@bot.message_handler(content_types=["photo"])
def handle_docs_photo(message):
    bot.reply_to(message, "this is photo.")


# handle all sent video
@bot.message_handler(content_types=["video"])
def handle_docs_video(message):
    bot.reply_to(message, "this is video.")


# handle all sent voice
@bot.message_handler(content_types=["voice"])
def handle_docs_voice(message):
    bot.reply_to(message, "this is voice.")


# handle all other messages for wich the lambda
# returns true.
# (true whe there is a document and is if this is type text/plain)
@bot.message_handler(func=lambda
                     message: message.document.mime_type == 'text/plain',
                     content_types=['document'])
def handle_text_doc(message):
    bot.reply_to(message, "this document is type 'text/plain'")


# handle all sent document
@bot.message_handler(content_types=["document"])
def handle_docs_doc(message):
    bot.reply_to(message, "this is document.")


# handle all sent sticker
@bot.message_handler(content_types=["sticker"])
def handle_docs_sticker(message):
    bot.reply_to(message, "this is sticker.")


# handles all text messages that match the regular
# expression with regexp
@bot.message_handler(regexp="^Book")
def handle_text(message):
    bot.reply_to(message, "I love books.")


# handle all text
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     bot.reply_to(message, "this is message.text: " + message.text)




# wich could also be defined as
def is_textPlain(message):
    return message.document.mime_type == 'text/plain'


@bot.message_handler(func=is_textPlain, content_types=['document'])
def handle_text_doc(message):
    bot.reply_to(message, "this document is type 'text/plain' - seccon way")


# handlers can be stacked to create a function wich be
# called if either message_handler is eligible
# this handler will be called if the message start with '/hellor'
# or is some emoji
@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda message: '👋' in message.text)
def send_hello(message):
    bot.reply_to(message, "Hello!")


#####
# edited messages handlers
# passes a Message type object to your function
@bot.edited_message_handler(func=lambda message: True)
def echo_edited(message):
    bot.reply_to(message, "you edited message")


# channel post handler
# passes a Message type object to your function
@bot.channel_post_handler(func=lambda message: True)
def echo_channel(message):
    bot.reply_to(message, "you send channel message")


# edited channel post handler
# passes a Message type object to your function
@bot.edited_channel_post_handler(func=lambda message: True)
def echo_edited_channel(message):
    bot.reply_to(message, "you edited channel message")


######
# callback query handler
# passes a CallbackQuery type object to your function
@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    logger.info(call)


# shipping query handler
# passes a ShippingQuery type object to your function
@bot.shipping_query_handler(func=lambda query: True)
def test_shipping(query):
    logger.info(query)


# poll handler -> encuensta
# passes a Poll type object to your function
# @bot.poll_handler(func=lambda message: True)
@bot.message_handler(content_types=['poll'])
def create_poll(message):
    bot.send_message(message.chat.id, "you send poll")


# poll asnwer handler -> encuensta
# passes a PollAnswer type object to your function
@bot.poll_answer_handler()
def poll_answer(message):
    bot.reply_to(message, "you send poll answer")


####
# my chat menber handler
# passes a ChatMemberUpdated type object to your function
@bot.my_chat_member_handler()
def test_member(message):
    chat_id = message.chat.id
    new_status = message.new_chat_member.status
    if new_status == 'member':
        bot.send_message(chat_id, "hola soy el nuevo miembro :D")


# infinite loop
bot.infinity_polling(none_stop=True)

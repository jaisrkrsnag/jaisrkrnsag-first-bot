from typing import Text
import telebot

bot = telebot.TeleBot("2128337244:AAGyoDB3E-24c9X-1p58Er7zOcs_DBDQTyM")

@bot.message_handler(commands=['start', 'help', 'id'])
def send_welcome(message):
    chat_id= message.chat.id
    if "/start" in message.text:
        bot.send_message(chat_id, "Hello")
    elif "/help" in message.text:
        bot.send_poll(chat_id, "Hello How are YOu", ["Good", "Not Bad"], False, "quiz", False, 0, None, None, 30)
        bot.reply_to(message, "Howdy, how are you doing?")
    else:
        bot.reply_to(message, chat_id)
	
# @bot.message_handler(func=lambda message: "hello")
# def echo_all(message):
# 	bot.reply_to(message, message.text)

@bot.message_handler(content_types=['text'])
def handle_text_doc(message):
    if "hello" in message.text:
        chat_id=message.chat.id
        bot.reply_to(message, f"""This is the Study Group.
So, Don't Say Hii Hello {chat_id}""")




bot.infinity_polling()

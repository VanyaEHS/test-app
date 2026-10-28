import telebot
from telebot import apihelper
import webbrowser
from telebot import types
import sqlite3

apihelper.proxy = {'https': 'http://127.0.0.1:10809'}

bot = telebot.TeleBot('8679595371:AAE_HdKiWoDJBVPb8bRn7POhW2IEy83KHv4')

@bot.message_handler(commands=['start'], content_types=['text'])
def start(message):
  markup = types.InlineKeyboardMarkup() # Создаем кнопку
  btn1 = types.InlineKeyboardButton('Открыть приложение ', url='https://www.google.com/?hl=ru')
  markup.row(btn1)
  bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)

bot.infinity_polling(timeout=10, long_polling_timeout=5)
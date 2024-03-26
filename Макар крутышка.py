import telebot
from telebot import types

def choose (chatid):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton('Крутить барабан'))
    kb.add(types.KeyboardButton('Назвать слово'))
    kb.add(types.KeyboardButton('Назвать букву'))
    bot.send_message(chatid, "Выбирете действие:", reply_markup=kb)








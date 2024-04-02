import telebot
from telebot import types
games = {}

bot = telebot.TeleBot("6736959406:AAFwdUBqmBybnmoEZKzB3eau0v2dXO3cOwo")

@bot.message_handler(commands=["start"])
def test(m):
    if proverka() == True:
     bot.send_message(m.chat.id,"Игра началась!")
    else:
        bot.send_message(m.chat.id, "Игра еще не началась!")



@bot.message_handler(commands=["hello"])
def test(m):
    bot.send_message(m.chat.id,"Приветствую вас!")


def choose (chatid):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton('Крутить барабан'))
    kb.add(types.KeyboardButton('Назвать слово'))
    kb.add(types.KeyboardButton('Назвать букву'))
    bot.send_message(chatid, "Выбирете действие:", reply_markup=kb)

def proverka(players, game):
    if len(players) > 3:
        if not game["srart"]:
            return True
        return  False
    return False













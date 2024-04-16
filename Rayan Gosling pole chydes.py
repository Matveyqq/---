import telebot
from telebot import types
import random
games = {}

bot = telebot.TeleBot("6736959406:AAFwdUBqmBybnmoEZKzB3eau0v2dXO3cOwo")

@bot.message_handler(commands=["start"])
def test(m):
    if proverka() == True:
     bot.send_message(m.chat.id,"Игра началась!")
    else:
        bot.send_message(m.chat.id, "Игра еще не началась!")


@bot.message_handler(commands=["join"])
def join(m):
    if m.chat.id not in games:
        bot.send_message(m.chat.id, "Игры нет!")
        return
    game = games[m.chat.id]
    if m.from_user.id not in game["players"]:
        bot.send_message(m.chat.id, "Вы зашли!")
    else:
        bot.send_message(m.chat.id, "Вы уже в игре!")



@bot.message_handler(commands=["hello"])
def test(m):
    bot.send_message(m.chat.id,"Приветствую вас!")


@bot.message_handler()
def fdgfdg(m):
        if get_current_player == m.from_user.id:
            if m.text == "крутить барабан":
                roll_drum()
            if m.text == "назвать слово":
                name_word()
            if m.text == "назвать букву":
                name_letter()
        else:
            bot.send_message(m.chat.id,"Этот ход не ваш! Иди плачь.")

def choose (chatid):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton('Крутить барабан'))
    kb.add(types.KeyboardButton('Назвать слово'))
    kb.add(types.KeyboardButton('Назвать букву'))
    bot.send_message(chatid, "Выбирете действие:", reply_markup=kb)


def podgotovka (chatid):
     set_started(chatid)
     allplayers = get_players(chatid)
     listplayers = []
     for player in allplayers:
        listplayers.append(player)
     randomplayer = random.choice(listplayers)
     set_current_player(chatid, randomplayer)

def proverka(players, game):
    if len(players) > 3:
        if not game["srart"]:
            return True
        return  False
    return False













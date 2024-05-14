import telebot
from telebot import types
import random
import get_game
games = {}
import traceback

bot = telebot.TeleBot("6736959406:AAFwdUBqmBybnmoEZKzB3eau0v2dXO3cOwo")
print(bot.get_me())

@bot.message_handler(commands=["start"])  # эта функция начинает игру
def test(m):
    try:
        game = get_game.get_game(m.chat.id, games)
        players = get_game.get_players(m.chat.id, games)
        if proverka(players, game) == True:
         bot.send_message(m.chat.id,"Игра началась!")
         get_game.set_started(m.chat.id, games)
         perexod(players, game)

        else:
            bot.send_message(m.chat.id, "Игра еще не началась!")
    except:
        print(traceback.format_exc())
        bot.send_message(m.chat.id, "Вы ошиблись дверью")

@bot.message_handler(commands = ['podgotovka'])
def podgotovka(m):
    game = create_game(m.chat.id)
    games[m.chat.id] = game
    bot.send_message(m.chat.id, "Игра создана.")

@bot.message_handler(commands=["join"]) # эта фукция позваляет игрокам зайти в игру
def join(m):
    if m.chat.id not in games:
        bot.send_message(m.chat.id, "Игры нет!")
        return
    game = games[m.chat.id]
    if m.from_user.id not in game["players"]:
        player = create_player(m.from_user.id, m.from_user.first_name)
        game["players"][m.from_user.id] = player
        bot.send_message(m.chat.id, "Вы зашли!")

    else:
        bot.send_message(m.chat.id, "Вы уже в игре!")



@bot.message_handler(commands=["hello"]) 
def test(m):
    bot.send_message(m.chat.id,"Приветствую вас!")

def name_word(m):
    game = get_game.get_game(m.chat.id, games)
    if game["word"] == True:
            if m.text == game["full_word"]:
                end_game(game)
            else:
                bot.send_message(m.chat.id, "Поздравляю!Вы вылетаете отсюда бездарь!")
                del games[m.from_user.id]

@bot.message_handler()
def fdgfdg(m):
    try:
        game = get_game.get_game(m.chat.id, games)
        if game["word"] == True:
            name_word(m)
            game["word"] = False
        if game["letter"] == True:
            proverka_letter(m)
            game["letter"] = False
        if get_game.get_current_player(m.chat.id, games) == m.from_user.id:
            if m.text == "Крутить барабан":
                prokrutka_barabana(m)
            if m.text == "Назвать слово":
                game["word"] = True
                bot.send_message(m.chat.id, "А теперь назовите слово:")
            if m.text == "Назвать букву":
                game["letter"] = True
                bot.send_message(m.chat.id, "А теперь назовите букву:")
        else:
            bot.send_message(m.chat.id,"Этот ход не ваш! Иди поплачь лысый.")
    except:
        pass
            




def end_game(game):
    bot.send_message(game["id"], " Раян Гослинг Сигма Слово Пацана! Вы победили!")
    del games[game["id"]]

def choose (chatid):
    kb = types.ReplyKeyboardMarkup()
    kb.add(types.KeyboardButton('Крутить барабан'))
    kb.add(types.KeyboardButton('Назвать слово'))
    kb.add(types.KeyboardButton('Назвать букву'))
    bot.send_message(chatid, "Выбирете действие:", reply_markup=kb)


def podgotovka (chatid):
     get_game.set_started(chatid, games)
     allplayers = get_game.get_players(chatid)
     listplayers = []
     for player in allplayers:
        listplayers.append(player)
     randomplayer = random.choice(listplayers)
     get_game.set_current_player(chatid, games, randomplayer)

def proverka_letter(m):# проверяет букву
    game = get_game.get_game(m.chat.id, games)
    players = get_game.get_players(m.chat.id, games)
    if game["letter"] == True:#если буква верна
        if (m.text in game["full_word"]):# если в тв тексте в полно слове
            bot.send_message(m.chat.id, "Боже лакер,есть такая буква.")

        else:
            bot.send_message(m.chat.id, "Твое мнение не учитывается,СЭР ДА СЭР, ход отдается другому игроку.")
            perexod(players, game)#вызов функции
def perexod(players, game):# осушествляет переход хода к другому игроку
        u=False
        x = False
        for player in players:
            if x ==True:# если х верен
                game["current_player"] = player# курент плаер равно праер
                u=True
                choose(game["id"])
                break# остановка
            if player == game ["current_player"]:# если игрок равен курент плаер
                x = True# х верен
        if u == False:# если u ложная
            for player in players:
                game["current_player"] = player# курент плаер равен игроку
                choose(game["id"])
                break# остановка

list = [0,350,400,450,500,550,600,650,700,850,900,950,1000,"сектор СИГМА","сектор ПРИЗ","банкрот","сектор ПЛЮС"]
points = 0

def prokrutka_barabana(m): # Функция прокрутки барабана,Матвей
    list = [0, 350, 400, 450, 500, 550, 600, 650, 700, 850, 900, 950, 1000, "сектор СИГМА", "сектор ПРИЗ", "банкрот",
            "сектор ПЛЮС"]
    game = get_game.get_game(m.chat.id, games)
    players = get_game.get_players(m.chat.id, games)
    player = get_game.get_player(m.chat.id, games, m.from_user.id)
    points = 0
    choose = random.choice(list)
    print(choose)
    if type(choose) == int: # Если выбор равен инт то к очкам прибовляется то что выпало на барабане
        points += choose
        bot.send_message(m.chat.id,f"Вы получили {choose} баллов")
        player["points"] += choose
        bot.send_message(m.chat.id, f"Ваши баллы: {player["points"]}")
        perexod(players, game)
    else:
        if choose == "сектор СИГМА":
            player["points"] *= 2
            bot.send_message(m.chat.id, f"Ваши баллы умножены на 2!")
            bot.send_message(m.chat.id, f"Ваши баллы: {player["points"]}")
            perexod(players, game)
    if choose == "банкрот":
        player["points"] = 0
        bot.send_message(m.chat.id, f"Ваши баллы сгорели!")
        bot.send_message(m.chat.id, f"Ваши баллы: {player["points"]}")
        perexod(players, game)


def proverka(players, game):
    if len(players) > 0:
        if not game["started"]:
            return True
        return  False
    return False


def create_game(chatid):
    game = {
        "players": {

        },
        "started": False,
        "current_player": 12345,
        "word": False,
        "letter": False,
        "full_word": "test",
        "id":chatid
    }
    return game

def create_player(pid, pname):
    player={
    "id":pid,
    "name":pname,
    "points":0
    }
    return player



bot.infinity_polling()




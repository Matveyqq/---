import telebot
from telebot import types
import random
import get_game
games = {}

bot = telebot.TeleBot("7150377743:AAF310LRUw9NTRqHp6yaUWunRaTpuLeGF9Y")

@bot.message_handler(commands=["start"])  # эта функция начинает игру
def test(m):
    game = get_game.get_game(m.chat.id, games)
    players = get_game.get_players(m.chat.id, games)
    if proverka(players, game) == True:
     bot.send_message(m.chat.id,"Игра началась!")
     get_game.set_started(m.chat.id, games)
     choose(m.chat.id)

    else:
        bot.send_message(m.chat.id, "Игра еще не началась!")

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
    game = get_game.get_game(m.chat.id)
    if game["word"] == True:
        if game["full_word"] == True:
            if m.text == game["full_word"]:
                end_game()
            else:
                bot.send_message(m.chat.id, "Поздравляю!Вы вылетаете отсюда бездарь!")
                del games[m.from_user.id]

@bot.message_handler()
def fdgfdg(m):
        if get_game.get_current_player == m.from_user.id:
            if m.text == "крутить барабан":
                prokrutka_barabana(m)
            if m.text == "назвать слово":
                name_word(m)
            if m.text == "назвать букву":
                proverka_letter(m)
        else:
            bot.send_message(m.chat.id,"Этот ход не ваш! Иди плачь.")
            




def end_game(m):
    bot.send_message(m.from_user.id, " побеждает!Поздравляем!")
    del games[m.chat.id]

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
    game = get_game.get_game(m.chat.id)
    players = get_game.get_players(m.chat.id)
    if game["letter"] == True:#если буква верна
        if (m.text in game["full_word"]):# если в тв тексте в полно слове
            bot.send_message(m.chat.id, "Есть такая буква.")

    else:
        bot.send_message(m.chat.id, "Буква не правильная, ход отдается дкугому игроку.")
        perexod(players, game)#вызов функции
def perexod(players, game):# осушествляет переход хода к другому игроку
        u=False
        for player in players:
            if x ==True:# если х верен
                game["current_player"] = player# курент плаер равно праер
                u=True
                break# остановка
            if player == game ["current_player"]:# если игрок равен курент плаер
                x = True# х верен
        if u == False:# если u ложная
            for player in players:
                game["current_player"] = player# курент плаер равен игроку
                break# остановка

list = [0,350,400,450,500,550,600,650,700,850,900,950,1000,"сектор СИГМА","сектор ПРИЗ","банкрот","сектор ПЛЮС"]
points = 0

def prokrutka_barabana(m): # Функция прокрутки барабана,Матвей
    list = [0, 350, 400, 450, 500, 550, 600, 650, 700, 850, 900, 950, 1000, "сектор СИГМА", "сектор ПРИЗ", "банкрот",
            "сектор ПЛЮС"]
    game = get_game.get_game(m.chat.id)
    players = get_game.get_players(m.chat.id, games)
    points = 0
    choose = random.choice(list)
    print(choose)
    if type(choose) == int: # Если выбор равен инт то к очкам прибовляется то что выпало на барабане
        points += choose
        bot.send_message(m.chat.id,f"Вы получили {choose} баллов")
        perexod(players, game)
    else:
        if choose == "сектор СИГМА":
            print *2
    if choose == "банкрот":
        points = 0


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
    "name":pname
    }
    return player



bot.infinity_polling()




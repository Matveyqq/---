def get_game(chatid):#возвращает словарь
    game = games[chatid]
    return game

def get_players(chatid):
    game = games[chatid]
    players = game["players"]
    return players

def get_started(chatid):
    game = games[chatid]
    started = game["start"]
    return started

def get_current_player(chatid):
    game = games[chatid]
    current_player = game["current_player"]
    return current_player

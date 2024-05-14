def get_game(chatid, games):
    game = games[chatid]
    return game

def get_players(chatid, games):
    game = games[chatid]
    players = game["players"]
    return players

def get_player(chatid, games, playerid):
    game = games[chatid]
    players = game["players"]
    player = players[playerid]
    return player

def get_started(chatid, games):
    game = games[chatid]
    started = game["start"]
    return started

def set_started(chatid, games):
    game = games[chatid]
    game["start"] = True


def get_current_player(chatid, games):
    game = games[chatid]
    current_player = game["current_player"]
    return current_player

def set_current_player(chatid, games, player):
    game = games[chatid]
    game["current_player"] = player


def get_word(chatid, games):
    game = games[chatid]
    word = game["word"]
    return word

def get_letter(chatid, games):
    game = games[chatid]
    letter = game["letter"]
    return letter

def get_game(chatid):
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

def get_word(chatid):
    game = games[chatid]
    word = game["word"]
    return word

def get_letter(chatid):
    game = games[chatid]
    letter = game["letter"]
    return letter

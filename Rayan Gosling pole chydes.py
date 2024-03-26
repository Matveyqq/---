
import telebot


bot = telebot.TeleBot("6736959406:AAFwdUBqmBybnmoEZKzB3eau0v2dXO3cOwo")

@bot.message_handler(commands=["start"])
def test(m):
    bot.send_message(m.chat.id,"Игра началась!")


@bot.message_handler(commands=["hello"])
def test(m):
    bot.send_message(m.chat.id,"Приветствую вас!")













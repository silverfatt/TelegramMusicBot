from functions import *
from threading import Thread


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    """
    Handler for /start command
    :param message: message from user
    :return: None
    """
    bot.send_message(message.chat.id, "Hey! Just send me title of song and you will get it")
    print(f"{message.from_user.full_name}: {message.text}")


@bot.message_handler()
def find_music(message: telebot.types.Message):
    """
    Handler for all other messages
    :param message: message from user
    :return: None
    """
    th = Thread(target=serve_user, args=(message,))
    th.start()


bot.polling(none_stop=True)

import os
import telebot
from parse import *

bot = telebot.TeleBot('5719168851:AAFsyBNALIggcpY7oX5PKx9bs1Ie9TF-yyU')

# Directory where songs will be temporarily stored, could be changed
source = "/Users/Admin/Downloads/"


def serve_user(message: telebot.types.Message):
    """
    Serves user - sends music to him
    or gives usage information
    :param message: message from user
    :return: None
    """
    print(f"{message.from_user.full_name} : {message.text} : {message.id}")
    if message.text.lower() == '/help':
        bot.send_message(message.chat.id, "Just send me title of song and you will get it")
    elif message.text[0] == '/':
        bot.send_message(message.chat.id, "I don't support that command")
    else:
        try:
            url = request_page(message.text)
            filename = f"{message.from_user.id}${message.id}.mp3"
            audiofile = requests.get(url)
            try:
                with open(f'{source}{filename}', 'wb') as f:
                    f.write(audiofile.content)
                    print(f"Installed {filename}")
            except OSError:
                print('Could not download song')
            print(f"Sending {filename}")
            bot.send_audio(message.chat.id, audio=open(f'{source}{filename}', 'rb'))
            print(f"Sent {filename}")
            if os.path.isfile(f'{source}{filename}'):
                os.remove(f'{source}{filename}')
                print(f"Deleted {filename}")
        except TypeError:
            bot.send_message(message.chat.id, 'Could not find a song')
            print("Could not find a song")

# TelegramMusicBot

![image](https://user-images.githubusercontent.com/90452368/189527606-8f917fd6-5293-4c4f-8292-a97d631c6591.png)

### Description

Simple telegram bot that finds music for you.

Bot gets name of song, finds it, downloads to server storage (probably your computer), sends to user and deletes from storage.

### Installation
1) Clone repository
2) Open terminal and run `pip install requirements.txt`

### Launch

Open terminal and run `python main.py`

Don't forget to get a token of your bot and add it to `functions.py`:

```python
bot = telebot.TeleBot('YOUR-TOKEN-HERE')
```

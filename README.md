# TelegramMusicBot

![image](https://user-images.githubusercontent.com/90452368/189527606-8f917fd6-5293-4c4f-8292-a97d631c6591.png)

### Description

Simple telegram bot that finds music for you.

Bot gets name of song, finds it, installs, sends to user and deletes it.

### Installation
1) clone repository
2) open terminal and run `pip install requirements.txt`

### Launch

Open terminal and run `python main.py`

Don't forget to get a token of your bot and add it to `functions.py`:

```python
bot = telebot.TeleBot('YOUR-TOKEN-HERE')
```

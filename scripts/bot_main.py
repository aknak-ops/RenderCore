import telebot
import json
from commands import start_batch, stop_batch, get_status

with open("config.json") as f:
    config = json.load(f)

bot = telebot.TeleBot(config["token"])

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "RenderCore Bot Activated. Use /run or /status.")

@bot.message_handler(commands=['run'])
def run_batch(message):
    output = start_batch()
    bot.reply_to(message, output)

@bot.message_handler(commands=['stop'])
def stop_batch_cmd(message):
    output = stop_batch()
    bot.reply_to(message, output)

@bot.message_handler(commands=['status'])
def system_status(message):
    output = get_status()
    bot.reply_to(message, output)

bot.polling()

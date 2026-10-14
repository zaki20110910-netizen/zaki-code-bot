
import os
import telebot

TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(TOKEN)

def convert(text):
    text = text.replace("_", "")
    if text.startswith("fh"):
        text = "wlan" + text[2:]

    swaps = {
        "6": "9", "9": "6",
        "7": "8", "8": "7",
        "a": "5", "5": "a",
        "b": "4", "4": "b",
        "d": "2", "2": "d",
        "c": "3", "3": "c",
        "f": "0", "0": "f",
        "1": "e", "e": "1",
    }
    return "".join(swaps.get(ch, ch) for ch in text)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "أهلا! ابعث الرمز لتحويله.")

@bot.message_handler(func=lambda m: bool(m.text))
def handle(message):
    bot.reply_to(message, convert(message.text.strip()))

bot.infinity_polling(skip_pending=True)

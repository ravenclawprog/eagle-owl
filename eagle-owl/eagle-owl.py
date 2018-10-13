import command_mode
import config
import sys, signal
import telebot
from telebot.types import Message
from telebot import apihelper
from threading import Thread
import time

#не забудьте указать в config.py 
#TOKEN - токен вашего бота
#PROXY - адреса прокси, если такой необходим
if config.PROXY != '':
	telebot.apihelper.proxy = {
    	'https': f'{config.PROXY}'
	}

stop_yeah = False
myTime = 120
L = 0

def set_StopYeah(arg):
	global stop_yeah
	stop_yeah = arg

def get_StopYeah():
	return stop_yeah


def set_L(arg):
	global L
	L = arg

def get_L():
	return L

def signal_handler(signal, frame):
	set_StopYeah(True)
	print("\n Бот покинул здание")
	sys.exit(0)

def yeah_function():
    start = time.time()
    while not get_StopYeah():
	    end = time.time()
	    if (end-start) > myTime:
			    start = end
			    if command_mode.bot_state == 1:
				    bot.send_message(get_L(), "Угу")

set_L(0)
set_StopYeah(False)

signal.signal(signal.SIGINT, signal_handler)

bot = telebot.TeleBot(config.TOKEN, threaded=False)

thread = Thread(target = yeah_function, args = ())
thread.start()

@bot.message_handler(commands=['start'])
def start_command(message):
	command_mode.bot_state = 1
	set_L(message.chat.id)
	bot.send_message(message.chat.id, command_mode.start())	

@bot.message_handler(commands=['stop'])
def stop_command(message):
	command_mode.bot_state = 2
	set_L(message.chat.id);
	bot.send_message(message.chat.id, command_mode.stop())

@bot.message_handler(commands=['send_location'])
def send_location(message):
	bot.send_message(message.chat.id, "Я здесь")
	payload = [39.032487, 125.752385]
	bot.send_location(message.chat.id, payload[0], payload[1])

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): 
	if command_mode.bot_state == 1:
		if "подтверди" in message.text.lower():
			bot.send_message(message.chat.id, "Подтверждаю")
		else:
			bot.send_message(message.chat.id, "Угу")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e) # или просто print(e) если у вас логгера нет,
       	time.sleep(15)


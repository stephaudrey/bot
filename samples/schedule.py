import sys
import time
import telepot
from telepot.loop import MessageLoop
import splinter
import os
import sys

reply_dict = {
    'hi': 'hi',
    'hello': 'Hello',
    'good morning': 'Good morning',
    'good afternoon': 'Good afternoon',
    'good evening': 'Good evening',
    'good night': 'Good night',
    'good day': 'Good day',
    'who created you?': 'Awesome people named Jason, Hans, Audrey, Gaby, and Dennis :)',
    'who created you': 'Awesome people named Jason, Hans, Audrey, Gaby, and Dennis :)',
    'where are you from?':'I was made at NTU Singapore :) Pretty cool isnt it?',
    'where are you from':'I was made at NTU Singapore :) Pretty cool isnt it?',
    'how old are you?':'I was made sometime in September 2017',
    'how old are you':'I was made sometime in September 2017'
        }
second_reply = {
    'hi': 1,
    'hello': 1,
    'good morning': 1,
    'good afternoon': 1,
    'good evening': 1,
    'good night': 1,
    'good day': 1,
    'who created you?': 1,
    'who created you': 1,
    'where are you from?':1,
    'where are you from':1,
    'how old are you?':1,
    'how old are you':1
    }


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)  # debug msg received

    if content_type == 'text':
        response = bot.getUpdates()
        print(response)  # debug id response
        # bot.sendMessage(chat_id, msg['text'])
        msg_received = msg['text'].lower()
        print(msg['text'])  # debug input
        print(msg_received)  # debug lowered input
        if msg_received == '/start':
            print("bot started")
            bot.sendMessage(chat_id, "Hi! I'm a bot that tells you your course schedule and plan your meetings! Feel free to ask me stuff :)")
        elif msg_received == 'hi':
            bot.sendMessage(chat_id,reply_dict[msg_received]+', ' + response[0]['message']['from']['first_name']+'!')
        elif msg_received == 'hello':
            bot.sendMessage(chat_id,reply_dict[msg_received]+', ' + response[0]['message']['from']['first_name']+'!')
        elif msg_received == 'good morning':
            bot.sendMessage(chat_id,reply_dict[msg_received]+', ' + response[0]['message']['from']['first_name']+'!')
        elif msg_received == 'good afternoon':
            bot.sendMessage(chat_id,reply_dict[msg_received]+', ' + response[0]['message']['from']['first_name']+'!')
        elif msg_received == 'good evening':
            bot.sendMessage(chat_id,reply_dict[msg_received]+', ' + response[0]['message']['from']['first_name']+'!')
        elif msg_received == 'good night':
            bot.sendMessage(chat_id,reply_dict[msg_received]+', ' + response[0]['message']['from']['first_name']+'!')
        elif msg_received == 'good day':
            bot.sendMessage(chat_id,reply_dict[msg_received]+', ' + response[0]['message']['from']['first_name']+'!')
        elif msg_received in reply_dict:
            print(reply_dict[msg_received])  # debug reply
            if second_reply[msg_received] == 1:
                bot.sendMessage(chat_id, reply_dict[msg_received])
        else:
            bot.sendMessage(chat_id, "Sorry, I don't know what to reply to such conversation yet. :'( ")
        # print(response[0]['message']['from']['first_name']+response[0]['message']['from']['last_name'])

cwd = os.path.dirname(sys.argv[0])
path_file = cwd + '/a.txt'
f = open(path_file, "r")
token = (f.read())
f.close()
bot = telepot.Bot(token)

MessageLoop(bot, handle).run_as_thread()
print("Listening...")

# Keep the program running.
while 1:
    time.sleep(10)

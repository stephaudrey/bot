import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #response=getUpdates()
    #tuples=tuple(listofsem)
    if msg['text']=="meetings":
        inlines_keyboard=[[]]
        for i in range(0,len(days)) :
            print(days[i])
            inlines_keyboard.append([InlineKeyboardButton(text=days[i], callback_data=a[i])])
        keyboard = InlineKeyboardMarkup(inline_keyboard=inlines_keyboard)
        bot.sendMessage(chat_id, 'Choose a day!', reply_markup=keyboard)
        print(type(keyboard))
    
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    bot.answerCallbackQuery(query_id, text='Got it')
f=open("a.txt","r")
TOKEN= (f.read())
f.close()
# get token from txt
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')
while 1:
    time.sleep(10)

import telegram
import logging
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import InlineQueryHandler
from telegram.ext import CallbackQueryHandler


TOKEN='1164376458:AAEI4hOizvBq1TVAVs2zBLQiI4c9HNDGnT8'
bot=telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
Inlinebutton=telegram.InlineKeyboardButton
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Hola")
    print(update.effective_chat.first_name, update.effective_chat.last_name)

def fish(update, context):
    imgfish='https://i.redd.it/f3beijzc5nv21.jpg'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=imgfish, caption="Informacion de pesca")
    print("foto enviada")

def fishtime(update, context):
    imgtimefish='https://i.redd.it/stvrzc6c2xi41.jpg'
    strfishtime="""Tiempo para cocinar los peces:
    [Fish](https://reloj-alarma.es/temporizador/#countdown=00:00:45&enabled=0&seconds=45&title=The+fish+is+already+done!) = 45 seconds
    [Meat](https://reloj-alarma.es/temporizador/#countdown=00:01:05&enabled=0&seconds=65&title=The+fish+is+already+done!) (chicken, snake, pork, shark) = 65 seconds
    [Trophy Fish](https://reloj-alarma.es/temporizador/#countdown=00:01:35&enabled=0&seconds=95&title=The+fish+is+already+done!) = 95 seconds
    [Kraken](https://reloj-alarma.es/temporizador/#countdown=00:02:05&enabled=0&seconds=125&title=The+fish+is+already+done!) = 125 seconds
    [Megalodon](https://reloj-alarma.es/temporizador/#countdown=00:02:05&enabled=0&seconds=125&title=The+fish+is+already+done!) = 125 seconds
    

    Crate a timer presing in each item"""
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=imgtimefish, parse_mode= 'Markdown', caption=strfishtime)
    print('foto enviada a: '+update.message.from_user.first_name)

def talltales(update, context):
    buttonstalltales=[[Inlinebutton(text='The Shroudbreaker (Quest)', callback_data='theshroudbreakerquest')],
    [Inlinebutton(text='The Cursed Rogue', callback_data='TheCursedRogue')], 
    [Inlinebutton(text='The Legendary Storyteller', callback_data='TheLegendaryStoryteller')]]
    Inlinekeyboard_talltales=telegram.InlineKeyboardMarkup(buttonstalltales)
    context.bot.send_message(chat_id=update.effective_chat.id, text= 'Here we have the Tall Tales of '+
    'The Shroudbreaker Arc: \n',reply_markup= Inlinekeyboard_talltales)
    print(update.inline_query)

def urltest(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text="Para continuar toque [aquí](http://www.google.com/)")
    print("link enviado a" + update.effective_chat.first_name + update.effective_chat.last_name)

def inlineresult(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='yes, it works')
    print(update.callback_query.from_user)
    context.bot.answer_callback_query(update.callback_query.id)

inlineresult_handler=CallbackQueryHandler(inlineresult, pattern='theshroudbreakerquest')
urltest_handler=CommandHandler('urltest', urltest)
talltales_handler=CommandHandler('talltales', talltales)
start_handler=CommandHandler('start', start)
fish_hundler=CommandHandler('fish', fish)
fishtime_hundler=CommandHandler('fishtime', fishtime)

dispatcher.add_handler(inlineresult_handler)
dispatcher.add_handler(urltest_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(fish_hundler)
dispatcher.add_handler(fishtime_hundler)
dispatcher.add_handler(talltales_handler)

updater.start_polling()
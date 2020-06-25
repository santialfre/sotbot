import telegram
import logging
import text, re, tall_inlinekey
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
    strfishtime=text.fishtime+'\n\n Creates a timer presing in each item'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=imgtimefish, parse_mode= 'Markdown', caption=strfishtime)
    print('foto enviada a: '+update.message.from_user.username)

def talltales(update, context):
    buttonstalltales=[[Inlinebutton(text='The Shroudbreaker (Quest)', callback_data='tall_theshroudbreakerquest')],
    [Inlinebutton(text='The Cursed Rogue', callback_data='tall_theCursedRogue')], 
    [Inlinebutton(text='The Legendary Storyteller', callback_data='tall_theLegendaryStoryteller')]]
    Inlinekeyboard_talltales=telegram.InlineKeyboardMarkup(buttonstalltales)
    context.bot.send_message(chat_id=update.effective_chat.id, text= 'Here we have the Tall Tales of '+
    'The Shroudbreaker Arc: \n',reply_markup= Inlinekeyboard_talltales)
    print(update.inline_query)

#def urltest(update, context):
#    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text="Para continuar toque [aquí](http://www.google.com/)")
#    print("link enviado a" + update.effective_chat.first_name + update.effective_chat.last_name)

#### HANDLER MANAGE ####
inlineresult_handler=CallbackQueryHandler(tall_inlinekey.inlineresult, pattern=r"tall_")
#urltest_handler=CommandHandler('urltest', urltest)
talltales_handler=CommandHandler('talltales', talltales)
start_handler=CommandHandler('start', start)
fish_hundler=CommandHandler('fish', fish)
fishtime_hundler=CommandHandler('fishtime', fishtime)

dispatcher.add_handler(inlineresult_handler)
#dispatcher.add_handler(urltest_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(fish_hundler)
dispatcher.add_handler(fishtime_hundler)
dispatcher.add_handler(talltales_handler)

updater.start_polling()
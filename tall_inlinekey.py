import telegram
import text

def inlineresult(update, context):
    #context.bot.edit_message_reply_markup(chat_id=update.callback_query.message.chat.id, message_id=update.callback_query.message.message_id, reply_markup=telegram.InlineKeyboardMarkup([[]]))
    #Change for empty kayboard fo deleated message
    if update.callback_query.data == 'tall_theshroudbreakerquest':
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=text.theshroudbreakerquest_img, parse_mode='Markdown', 
        caption=text.theshroudbreakerquest_text+
        '\n\n Go to the [guide](https://rarethief.com/sea-of-thieves-the-shroudbreaker-tall-tale-guide/) if you need it.' )
        context.bot.deleteMessage(chat_id=update.callback_query.message.chat_id, message_id=update.callback_query.message.message_id)
        print('info for: '+update.callback_query.from_user.username)
        #print('Id: '+str(update.callback_query.message.message_id)) #In case of edit a message, add a photo to an existing message seams to be not possible
        context.bot.answer_callback_query(update.callback_query.id) #In any inline keyboard for remove the clock
    elif update.callback_query.data == 'tall_theCursedRogue':
        context.bot.send_message(chat_id=update.callback_query.message.chat_id, text='Yes. it works')
    else:
        context.bot.send_message(chat_id=update.callback_query.message.chat_id, text='There is no information at this momento for this tall tale.')
        context.bot.answer_callback_query(update.callback_query.id)

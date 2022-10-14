from telegram import Update 
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from db import users_collection
import uuid
 
# Bot
token = "TOKEN" 
updater = Updater(token, use_context=True) 
dispatcher = updater.dispatcher 
 
def start_handler(update: Update, context: CallbackContext):
    user_by_id = users_collection.find_one({"_id": update.effective_chat.id})
    
    if user_by_id != None:
        print("User already exists")
    else:
        print("New user")
        user = {
            "_id": update.effective_chat.id,
            "name": update.effective_chat.full_name,
            "movies": []
        }
        users_collection.insert_one(user)
        context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Hello, {update.effective_chat.first_name}!") 
 
def message_handler(update: Update, context: CallbackContext): 
    title = update.message.text
    movie = {
        "_id": str(uuid.uuid4()),
        "title": title
    }
    
    user = users_collection.find_one({"_id": update.effective_chat.id})
    
    seen = False
    for dbMovie in user["movies"]:
        if title.lower() == dbMovie["title"].lower():
            seen = True
    
    if seen:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ти це вже бачив.") 
    else:
        users_collection.update_one({"_id": update.effective_chat.id}, { "$push": {"movies": movie} })
        context.bot.send_message(chat_id=update.effective_chat.id, text="Добавлено новий фільм в список.")
 
start_command_handler = CommandHandler("start", start_handler) 
dispatcher.add_handler(start_command_handler) 
 
text_handler = MessageHandler(Filters.text & ~Filters.command, message_handler) 
dispatcher.add_handler(text_handler) 
 
# Start bot 
updater.start_polling()
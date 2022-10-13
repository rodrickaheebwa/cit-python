import os
#python-telegram-bot
import telegram.ext
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN1')

todos = []

def start(update, context):
    update.message.reply_text("Hello! I am a friendly developer evaluation bot!")
    update.message.reply_text("What is your name?")

def help(update, context):
    update.message.reply_text("I am here to help you")

def search(update, context):
    update.message.reply_text("I am browsing google")

def music(update, context):
    update.message.reply_text("I am looking for music")

def display(update, context):
    for item in todos:
        update.message.reply_text(item)

def message_handler(update, context):
    if update.message.text == 'start':
        start(update, context)
    update.message.reply_text(f"You said {update.message.text}")

def add_todo(update, context):
    todo = ' '.join(context.args[0:])
    todos.append(todo)
    print(todos)
    update.message.reply_text(f"You added a todo: {todo}")
    update.message.reply_text(f"At what time do you wish to start: {todo}")

def menu(update, context):
    options = {
        '/display':'diplay to do list',
        '/search' : 'google anything',
        '/music' : 'recommend music'
    }
    output = ''
    for key, value in options.items():
        output += key + ' : ' + value + '\n'
    update.message.reply_text(f"---- MENU ----\n{output}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("menu", menu))
disp.add_handler(telegram.ext.CommandHandler("add", add_todo))
disp.add_handler(telegram.ext.CommandHandler("display", display))
disp.add_handler(telegram.ext.CommandHandler("search", search))
disp.add_handler(telegram.ext.CommandHandler("music", music))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))

updater.start_polling()
updater.idle()
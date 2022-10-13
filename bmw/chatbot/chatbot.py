import nltk
from nltk.chat.util import Chat, reflections
import telegram.ext
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN2')

print(Chat)

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name?",
        ["You can call me a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?","what is your name as well?"]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?",]
    ],
    [
        r"how can i help you? ",
        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear","How can i help you?:)",]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Pluralsight is a great option to learn data science. You can check their website",]
    ],
    [
        r"thanks for the suggestion. do they have great authors and instructors?",
        ["Yes, they have the world class best authors, that is their strength;)",]
    ],
    [
        r"(.*) thank you so much, that was helpful",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
     [
        r"(.*) Are you NZhima",
        ["Iam happy to help", "No problem, you're welcome",]
    ],
    [
        r"quit",
    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def chatbot():
        print("Hi, I'm the chatbot you built") 

chatbot()
chat = Chat(set_pairs, reflections)
#print(chat)
#chat.converse()
#print(chat.respond("Hello"))

def start(update, context):
    update.message.reply_text("Hello! I am a friendly developer evaluation bot!")
    update.message.reply_text("What is your name?")

def help(update, context):
    update.message.reply_text("I am here to help you")

def message_handler(update, context):
    user_input = update.message.text
    output = chat.respond(user_input)
    update.message.reply_text(f"{output}")

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, message_handler))

updater.start_polling()
updater.idle()

if __name__ == "__main__":
    chatbot()
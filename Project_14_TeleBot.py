import telebot
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_TOKEN = os.getenv('API_KEY')       #APi KEY IS IN ENV 

bot = telebot.TeleBot(API_TOKEN)

# Define command handlers

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Send a welcome message with a menu of available commands
    menu_text = (
        "Hello, Welcome to HAMOZA AI! Please choose an option:\n\n"
        "/start - Start the bot\n"
        "/help - Show help menu\n"
        "/content - About Resources\n"
        "/Python - Python Note\n"
        "/NumPy - NumPy Note\n"
        "/Pandas - Pandas Note\n"
        "/Matplotlib - Matplotlib Note\n"
        "/contact - Contact us\n"
    )
    bot.reply_to(message, menu_text)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Here are the commands you can use:\n"
        "/start - Start the bot\n"
        "/help - Show help menu\n"
        "/content - About Resources\n"
        "/Python - Python Note\n"
        "/NumPy - NumPy Note\n"
        "/Pandas - Pandas Note\n"
        "/Matplotlib - Matplotlib Note\n"
        "/contact - Contact us\n"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['content'])
def send_content(message):
    bot.reply_to(message, "Content:\n")

@bot.message_handler(commands=['Python'])
def send_python_note(message):
    bot.reply_to(
        message,
        "Python Note Drive Link: https://drive.google.com/file/d/1yO87Ly0yrmA2qNpa7cPknGbDA2e1r5nD/view?usp=drive_link\n"
    )

@bot.message_handler(commands=['NumPy'])
def send_numpy_note(message):
    bot.reply_to(
        message,
        "NumPy Drive Link: https://colab.research.google.com/drive/1kYo7Wj7qwhVL4z4eu8FNk8eZbS5BW3IU?usp=drive_link\n"
    )

@bot.message_handler(commands=['Pandas'])
def send_pandas_note(message):
    bot.reply_to(
        message,
        "Pandas Drive Link: https://colab.research.google.com/drive/1mPXuXHDgk3y9i5JxDS0SWRLy88s94lds?usp=drive_link\n"
    )

@bot.message_handler(commands=['Matplotlib'])
def send_matplotlib_note(message):
    bot.reply_to(
        message,
        "Matplotlib Drive Link: https://colab.research.google.com/drive/1mPXuXHDgk3y9i5JxDS0SWRLy88s94lds?usp=drive_link\n"
    )

@bot.message_handler(commands=['contact'])
def send_contact_info(message):
    bot.reply_to(message, "Contact us at: jayed2305101640@diu.edu.bd")

# Start the bot
bot.infinity_polling()

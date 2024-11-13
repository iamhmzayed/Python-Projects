import telebot
from dotenv import load_dotenv
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key
API_TOKEN = os.getenv('API_KEY')

# Initialize bot with the API token
bot = telebot.TeleBot(API_TOKEN)

# Define the main menu text
menu_text = "Hello, Welcome to HAMOZA AI! Please choose an option:"

# Define a function to create the main menu keyboard
def create_main_menu():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Start the bot", callback_data="start"),
        InlineKeyboardButton("About Resources", callback_data="content"),
        InlineKeyboardButton("Contact us", callback_data="contact")
    )
    return markup

# Command Handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, menu_text, reply_markup=create_main_menu())

@bot.message_handler(commands=['content'])
def send_content(message):
    # Content keyboard with specific note links
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("Python Note", callback_data="Python"),
        InlineKeyboardButton("NumPy Note", callback_data="NumPy"),
        InlineKeyboardButton("Pandas Note", callback_data="Pandas"),
        InlineKeyboardButton("Matplotlib Note", callback_data="Matplotlib")
    )
    bot.send_message(message.chat.id, "Choose a resource:", reply_markup=markup)

# Dictionary of note links
notes_links = {
    'Python': "https://drive.google.com/file/d/1yO87Ly0yrmA2qNpa7cPknGbDA2e1r5nD/view?usp=drive_link",
    'NumPy': "https://colab.research.google.com/drive/1kYo7Wj7qwhVL4z4eu8FNk8eZbS5BW3IU?usp=drive_link",
    'Pandas': "https://colab.research.google.com/drive/1mPXuXHDgk3y9i5JxDS0SWRLy88s94lds?usp=drive_link",
    'Matplotlib': "https://colab.research.google.com/drive/1mPXuXHDgk3y9i5JxDS0SWRLy88s94lds?usp=drive_link"
}

@bot.message_handler(commands=['contact'])
def send_contact_info(message):
    bot.reply_to(message, "Contact us at: jayed2305101640@diu.edu.bd")

# Callback handler for inline buttons
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "start":
        # Display main menu again after selecting "Start the bot"
        bot.send_message(call.message.chat.id, menu_text, reply_markup=create_main_menu())
    elif call.data == "content":
        # Display content selection again after choosing "About Resources"
        send_content(call.message)
    elif call.data == "contact":
        # Display contact info, then main menu again
        send_contact_info(call.message)
        bot.send_message(call.message.chat.id, menu_text, reply_markup=create_main_menu())
    elif call.data in notes_links:
        # Send the link for the selected note and display main menu again
        bot.send_message(call.message.chat.id, f"{call.data} Note Drive Link: {notes_links[call.data]}")
        bot.send_message(call.message.chat.id, menu_text, reply_markup=create_main_menu())

# Start polling
bot.infinity_polling()

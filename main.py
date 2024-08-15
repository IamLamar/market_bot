import telebot
from telebot import types
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    welcome_text=("Здравствуйте, приветствую вас")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("Телефоны","Планшеты","Ноутбуки")
    bot.send_message(message.chat.id,welcome_text,reply_markup=markup)

@bot.message_handler(func=lambda message: message.text in ["Телефоны","Планшеты","Ноутбуки"])
def handle_message(message):
    if message.text == "Телефоны":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Iphone 15 Pro max 100,000 som", callback_data='Iphone 15 Pro max 100,000 som'))
        markup.add(types.InlineKeyboardButton("Samsung Galaxy S22 Ultra 80,000 som", callback_data='Samsung Galaxy S22 Ultra 80,000 som'))
        bot.send_message(message.chat.id, "Выберите товар:", reply_markup=markup)
    elif message.text == "Планшеты":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("IPad 10 75,000 som",callback_data='IPad 10 75,000 som'))
        markup.add(types.InlineKeyboardButton("Samsung планшет S9 61,000 som",callback_data='Samsung планшет S9 61,000 som'))
        bot.send_message(message.chat.id, "Выберите товар:", reply_markup=markup)
    elif message.text == "Ноутбуки":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Asus ViviBook 30,000 som",callback_data='Asus ViviBook 30,000 som'))
        markup.add(types.InlineKeyboardButton("Lenovo tab m10 34,000 som",callback_data='Lenovo tab m10 30,000 som'))
        bot.send_message(message.chat.id, "Выберите товар:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "Iphone 15 Pro max 100,000 som":
        bot.send_photo(call.message.chat.id, open('iphone.png','rb'))
        bot.send_message(call.message.chat.id, "Вы выбрали Iphone 15 Pro max")
    elif call.data == "Samsung Galaxy S22 Ultra 80,000 som":
        bot.send_photo(call.message.chat.id, open('samsung.jpg','rb'))
        bot.send_message(call.message.chat.id,"Вы выбрали Samsung Galaxy S22 Ultra")
    elif call.data == "IPad 10 75,000 som":
        bot.send_photo(call.message.chat.id, open('ipad.jpeg','rb'))
        bot.send_message(call.message.chat.id,"Вы выбрали IPad 10")
    elif call.data == "Samsung планшет S9 61,000 som":
        bot.send_photo(call.message.chat.id, open('samsung_tablet.png','rb'))
        bot.send_message(call.message.chat.id,"Вы выбрали Samsung планшет S9")
    elif call.data == "Asus ViviBook 30,000 som":
        bot.send_photo(call.message.chat.id, open('asus.jpg','rb'))
        bot.send_message(call.message.chat.id,"Вы выбрали Asus ViviBook")
    elif call.data == "Lenovo tab m10 30,000 som":
        bot.send_photo(call.message.chat.id, open('lenovo.jpg','rb'))
        bot.send_message(call.message.chat.id,"Вы выбрали Lenovo tab m10")
    
bot.polling(non_stop=True)



    







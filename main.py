import telebot
from telebot.types import CallbackQuery

from markups import *

TOKEN = "5360346452:AAGPgZJDnCNwjDE_VLtNlIbQvz5S_AFFCgA"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
                     f"Приветсвую вас на наш тестовом боте", reply_markup=mainMenu())


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Каталог':
        msg = bot.send_message(message.from_user.id, "Вы перешли в каталог!", reply_markup=catalog_choice())
        bot.register_next_step_handler(msg, catalog_menu)
    elif message.text == 'Информация':
        msg1 = bot.send_message(message.from_user.id, 'Вы перешли в информацию')
        bot.register_next_step_handler(msg1, info_menu)


@bot.message_handler(func=lambda message: True)
def catalog_menu(message):
    if message.text == 'Товар1':
        bot.send_message(message.from_user.id, "Отлично!", reply_markup=choice_markup())
    elif message.text == 'Товар2':
        bot.send_message(message.from_user.id, "Отлично!", reply_markup=choice_markup())
    elif message.text == 'Товар3':
        bot.send_message(message.from_user.id, "Отлично!", reply_markup=choice_markup())
    elif message.text == 'Товар4':
        bot.send_message(message.from_user.id, "Отлично!", reply_markup=choice_markup())
    elif message.text == 'Товар5':
        bot.send_message(message.from_user.id, "Отлично!", reply_markup=choice_markup())


@bot.message_handler(func=lambda message: True)
def info_menu(message):
    bot.send_message(message.from_user.id, "Мы находимся в разработке поэтому инфы нет совсем....")


@bot.callback_query_handler(func=lambda call: True)
def call_Buy(call):
    if call.data == 'buy':
        bot.send_message(call.message.chat.id, 'Отлично товар в тестовой корзине')
        bot.answer_callback_query(call.id)
    elif call.data == 'info':
        bot.send_message(call.message.chat.id, 'Информация о товаре будет позже...')
        bot.answer_callback_query(call.id)


bot.polling(none_stop=True)

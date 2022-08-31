import telebot
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

""" Добавить покупку при нажатии кнопки inline режиме или показать инфу на товар."""
# @bot.callback_query_handlers()
# def buy(call):
#     if call.data == 'buy':
#         bot.answer_callback_query(call.id, 'Отлично товар в тестовой корзине')
#     elif call.data == 'info':
#         bot.answer_callback_query(call.id, 'Информация о товаре будет позже...')

bot.polling(none_stop=True)
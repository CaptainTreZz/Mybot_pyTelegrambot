import telebot

from markups import *
from database.database import *

TOKEN = "5360346452:AAGPgZJDnCNwjDE_VLtNlIbQvz5S_AFFCgA"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,
                     f"Приветсвую вас {message.from_user.first_name} в нашем тестовом боте\n"
                     f"Выберите нужные для вас раздел", reply_markup=mainMenu())


@bot.message_handler(content_types=['text'])
def main_menu(message):
    if message.text == 'Каталог':
        msg = bot.send_message(message.from_user.id, 'Вы перешли в раздел "Каталог"!', reply_markup=catalog_choice())
        bot.register_next_step_handler(msg, catalog_menu)
    elif message.text == 'Информация':
        bot.send_message(message.from_user.id, 'Вы перешли в раздел "Информацию"', reply_markup=info_menu())
    elif message.text == 'Регистрация':
        bot.send_message(message.from_user.id, 'Хорошо, перехожу в раздел "Регистрация"', reply_markup=register_users())


@bot.message_handler(content_types=['text'])
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
    elif message.text == 'Товар6':
        bot.send_message(message.from_user.id, "Отлично!", reply_markup=choice_markup())
    elif message.text == 'В главное меню':
        bot.send_message(message.from_user.id, "Переходим в главное меню", reply_markup=mainMenu())


@bot.callback_query_handler(func=lambda call: True)
def call_Buy(call):
    if call.data == 'buy':
        bot.send_message(call.message.chat.id, 'Отлично товар в тестовой корзине')
        bot.answer_callback_query(call.id)
    elif call.data == 'info':
        bot.send_message(call.message.chat.id, 'Информация о товаре будет позже...')
        bot.answer_callback_query(call.id)
    elif call.data == 'back':
        bot.send_message(call.message.chat.id, 'В главное меню')
        bot.answer_callback_query(call.id)
    elif call.data == 'next':
        us_id = call.from_user.id
        us_name = call.from_user.first_name
        us_surname = call.from_user.last_name
        db_table_val(user_id=us_id, name=us_name, surname=us_surname)
        bot.send_message(call.message.chat.id, 'Отлично вы зарегистрировались!')
        bot.answer_callback_query(call.id)
    elif call.data == 'not_next':
        bot.send_message(call.message.chat.id, 'Хорошо, продолжим без регистрации, '
                                               'но вам нужно обьязательно это сделать позже')
        bot.answer_callback_query(call.id)
    elif call.data == 'about':
        bot.send_message(call.message.chat.id, "Мы находимся в разработке поэтому инфы нет совсем....")
        bot.answer_callback_query(call.id)


bot.polling(none_stop=True)

from settings import *
from markup.markups import *
from database.database import *



# --- Приветствуем пользователя ---
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id,
                     f"Приветсвуем Вас в нашем тестовом telegram боте.\n"
                     f"Выберите нужные для вас раздел и нажмите на кнопку.", reply_markup=mainMenu())


# --- Меню 1 уровень ---
@bot.message_handler(content_types=['text'])
def main_Menu(message):
    if message.text == 'Каталог':
        msg = bot.send_message(message.from_user.id, 'Вы перешли в раздел "Каталог"!', reply_markup=catalog())
        bot.register_next_step_handler(msg, choice_mainMenu)
    elif message.text == 'Информация':
        bot.send_message(message.from_user.id, 'Вы перешли в раздел "Информация"', reply_markup=infoMenu())
    elif message.text == 'Регистрация':
        bot.send_message(message.from_user.id, 'Хорошо, перехожу в раздел "Регистрация"', reply_markup=register())


# --- Меню 2 уровень ---
@bot.message_handler(func=lambda message: True)
def choice_mainMenu(message):
    if message.text == 'Бочонок':
        if message.text == '1':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog1())
        elif message.text == '2':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog1())
        elif message.text == '3':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog1())
    elif message.text == 'Картон':
        if message.text == '1':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog2())
        elif message.text == '2':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog2())
        elif message.text == '3':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog2())
    elif message.text == 'Эмблема':
        if message.text == '1':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog3())
        elif message.text == '2':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog3())
        elif message.text == '3':
            bot.send_message(message.from_user.id, "Выберите товар", reply_markup=podcatalog3())


@bot.callback_query_handler(func=lambda call: True)
def call_buy(call):
    if call.data == 'buy':
        bot.send_message(call.message.chat.id, 'Отлично товар в тестовой корзине')
        bot.answer_callback_query(call.id)
    elif call.data == 'info':
        bot.send_message(call.message.chat.id, 'Информация о товаре будет позже...')
        bot.answer_callback_query(call.id)
    elif call.data == 'next':
        info = cur.execute(f'SELECT user_id FROM users WHERE user_id={call.from_user.id}')
        if info.fetchone() is None:
            # Делаем когда нету человека в бд
            us_id = call.from_user.id
            us_name = call.from_user.first_name
            db_table_user(user_id=us_id, name=us_name)
            bot.send_message(call.message.chat.id, 'Отлично вы зарегистрировались!', reply_markup=mainMenu())
            bot.answer_callback_query(call.id)
        else:
            # Делаем когда есть человек в бд
            bot.send_message(call.message.chat.id, 'Вы уже зарегистрированы!', reply_markup=mainMenu())
            bot.answer_callback_query(call.id)
    elif call.data == 'not_next':
        bot.send_message(call.message.chat.id, 'Хорошо, продолжим без регистрации, '
                                               'но вам нужно обьязательно это сделать позже', reply_markup=mainMenu())
        bot.answer_callback_query(call.id)
    elif call.data == 'about':
        bot.send_message(call.message.chat.id, "Мы находимся в разработке поэтому инфы нет совсем....",
                         reply_markup=mainMenu())
        bot.answer_callback_query(call.id)
    elif call.data == '1':
        bot.send_message(call.message.chat.id, '1', reply_markup=choice())
    elif call.data == '2':
        bot.send_message(call.message.chat.id, '2', reply_markup=choice())
        bot.answer_callback_query(call.id)
    elif call.data == '3':
        bot.send_message(call.message.chat.id, '3', reply_markup=choice())
        bot.answer_callback_query(call.id)
    elif call.data == 'back':
        bot.send_message(call.message.chat.id, 'В главное меню', reply_markup=mainMenu())
        bot.answer_callback_query(call.id)


bot.polling(none_stop=True)

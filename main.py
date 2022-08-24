from config import TOKEN, telebot, types
from database import add_user

bot = telebot.TeleBot(TOKEN)

text_messages = {
    'start':
    'Приветствую тебя, {name}!\n',
    'Я помогу тебе сделать онлайн заказ (это быстро и без очереди).\n\n'
    '1. Выбери интересующий товар\n'
    '2. Выбери время, когда захочешь забрать заказ\n'
    '3. Оплати заказ (это безопасно)\n'
    'about':
    'Я являюсь разработчиком данного проекта и все это сделал не я, если что бейте друга!!!'
}


# Приветсвуем пользователя.
@bot.message_handler(commands=['start', 'help'])
def menu_welcome(message):
    markup_start = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_start.row('Регистрация', 'Продолжить', 'Помощь', 'О нас')
    bot.send_message(message.from_user.id, text_messages['start'].format(name=message.from_user.first_name),
                     reply_markup=markup_start)


@bot.message_handler(content_types=['text'])
def register_user(message):
    if message.text == 'Регистрация':
        markup_reg = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_reg.row('Зарегистрироваться')
        msg = bot.send_message(message.from_user.id, "Нажмите клавишу Зарегистрироваться "
                                                     "и вы автоматически залогинитесь.",
                               reply_markup=markup_reg)
        bot.register_next_step_handler(msg, get_registration_messages)
    elif message.text == 'Помощь':
        msg1 = bot.send_message(message.from_user.id, "Просто пройдите регистрацию одним кликом и продолжите покупку.")
        bot.register_next_step_handler(msg1, register_user)

    elif message.text == 'О нас':
        markup_about = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_about.row('Назад')
        msg2 = bot.send_message(message.from_user.id, "Мы супер крутые ребята в любой момент придем к тебе "
                                                      "на помощь и не дадим твоему авто быть вкусным!!!",
                                reply_markup=markup_about)
        bot.register_next_step_handler(msg2, menu_welcome)
    elif message.text == 'Продолжить':
        markup_next = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_next.row('Назад')
        msg3 = bot.send_message(message.from_user.id, "Вы можете продолжить без регистрации но вам придется "
                                                       "это сделать при оформлении заказа, т.к. я не смогу угадать "
                                                       "куда вам отправить заказ.", reply_markup=markup_next)
        bot.register_next_step_handler(msg3, get_registration_messages)



@bot.message_handler(content_types=['text'])
def get_registration_messages(message):
    if message.text == 'Сделать заказ':
        bot.send_message(message.from_user.id, 'Привет! Ваше имя добавленно в базу данных!')
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    add_user(user_id=user_id, first_name=first_name, last_name=last_name)

    markup_go = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_go.row('Начать')
    reg1 = bot.send_message(message.from_user.id, "Отличном начнем попкупку", reply_markup=markup_go)
    bot.register_next_step_handler(reg1, catalogBoard)


# Выбор категории.
@bot.message_handler(content_types=['text'])
def catalogBoard(message):
    markup_ver = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_ver1 = types.KeyboardButton('Флакон')
    item_ver2 = types.KeyboardButton('Подвеска')
    item_ver3 = types.KeyboardButton('Картон')
    item_ver4 = types.KeyboardButton('Назад')
    markup_ver.add(item_ver1, item_ver2, item_ver3, item_ver4)
    msg = bot.send_message(message.from_user.id, "Пожалуйста выберите нужные вам раздел.", reply_markup=markup_ver)
    bot.register_next_step_handler(msg, catalog_selection)


# Выбор товара из выбранной категории.
@bot.message_handler(content_types=['text'])
def catalog_selection(message):
    select_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if message.text == 'Флакон':
        select_markup.row('Black', 'White', 'Red')
    elif message.text == 'Подвеска':
        select_markup.row('1', '2', '3')
    elif message.text == 'Картон':
        select_markup.row('11', '22', '33')
    elif message.text == 'Назад':
        msg_back = bot.send_message(message.from_user.id, 'Пожалуйста выберите нужные вам раздел.')
        bot.register_next_step_handler(msg_back, catalogBoard)

    msg = bot.send_message(message.from_user.id, 'Выберите нужные товар', reply_markup=select_markup)
    bot.register_next_step_handler(msg, product_selection)


# Выбираем товар и добавляем его в базу с предоставлением информации о товаре.
@bot.message_handler(content_types=['text'])
def product_selection(message):
    select_product = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Black':
        select_product.row('Заказать', 'Назад')
    elif message.text == 'White':
        select_product.row('Заказать', 'Назад')
    elif message.text == 'Red':
        select_product.row('Заказать', 'Назад')
    elif message.text == '1':
        select_product.row('Заказать', 'Назад')
    elif message.text == '2':
        select_product.row('Заказать', 'Назад')
    elif message.text == '3':
        select_product.row('Заказать', 'Назад')
    elif message.text == '11':
        select_product.row('Заказать', 'Назад')
    elif message.text == '22':
        select_product.row('Заказать', 'Назад')
    elif message.text == '33':
        select_product.row('Заказать', 'Назад')

    bot.send_message(message.from_user.id, 'Выбери товар и нажми заказать.', reply_markup=select_product)


bot.polling(none_stop=True)

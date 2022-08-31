from telebot import types

def mainMenu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Каталог', 'Информация', 'Регистрация')
    return markup


def catalog_choice():
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup1.row('Товар1', 'Товар2', 'Товар3')
    markup1.row('Товар4', 'Товар5', 'Товар6')
    markup1.row('В главное меню')
    return markup1


def choice_markup():
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    markup2.add(types.InlineKeyboardButton('Информация', callback_data='info'),
                types.InlineKeyboardButton('Купить', callback_data='buy'),
                types.InlineKeyboardButton('В главное меню', callback_data='back'))
    return markup2


def register_users():
    markup3 = types.InlineKeyboardMarkup(row_width=2)
    markup3.add(types.InlineKeyboardButton('Региструемся', callback_data='next'),
                types.InlineKeyboardButton('Без регистрации', callback_data='not_next'),
                types.InlineKeyboardButton('В главное меню', callback_data='back'))
    return markup3

def info_menu():
    markup4 = types.InlineKeyboardMarkup(row_width=2)
    markup4.add(types.InlineKeyboardButton('О нас', callback_data='about'),
                types.InlineKeyboardButton('В главное меню', callback_data='back'))
    return markup4


def delete():
    delete = types.ReplyKeyboardRemove()
    return delete
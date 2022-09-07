from telebot import types


# --- Главной меню ---
def mainMenu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(types.KeyboardButton('Каталог'),
               types.KeyboardButton('Информация'),
               types.KeyboardButton('Регистрация'))
    return markup


# --- Каталог ---
def catalog():
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup1.add(types.KeyboardButton('Бочонок'),
                types.KeyboardButton('Картон'),
                types.KeyboardButton('Эмблема'))
    return markup1


def register():
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    markup2.add(types.InlineKeyboardButton('Региструемся', callback_data='next'),
                types.InlineKeyboardButton('Без регистрации', callback_data='not_next'))
    return markup2


def infoMenu():
    markup3 = types.InlineKeyboardMarkup(row_width=2)
    markup3.add(types.InlineKeyboardButton('О нас', callback_data='about'))
    return markup3


# --- Подкаталог, товар1 ---
def podcatalog1():
    markup4 = types.InlineKeyboardMarkup(row_width=3)
    markup4.add(types.InlineKeyboardButton('Яблоко', callback_data='1'),
                types.InlineKeyboardButton('Лед', callback_data='2'),
                types.InlineKeyboardButton('Персик', callback_data='3'),
                types.InlineKeyboardButton('Назад', callback_data='back'))
    return markup4


# --- Подкаталог, товар2 ---
def podcatalog2():
    markup5 = types.InlineKeyboardMarkup(row_width=3)
    markup5.add(types.InlineKeyboardButton('Лед', callback_data='1'),
                types.InlineKeyboardButton('Елка', callback_data='2'),
                types.InlineKeyboardButton('Инструктор', callback_data='3'),
                types.InlineKeyboardButton('Назад', callback_data='back'))
    return markup5


# --- Подкаталог, товар3 ---
def podcatalog3():
    markup6 = types.InlineKeyboardMarkup(row_width=3)
    markup6.add(types.InlineKeyboardButton('МВД', callback_data='1'),
                types.InlineKeyboardButton('МЧС', callback_data='2'),
                types.InlineKeyboardButton('ВДВ', callback_data='3'),
                types.InlineKeyboardButton('Назад', callback_data='back'))
    return markup6


# --- Покупка товара ---
def choice():
    markup7 = types.InlineKeyboardMarkup(row_width=2)
    markup7.add(types.InlineKeyboardButton('Информация', callback_data='info'),
               types.InlineKeyboardButton('Купить', callback_data='buy'),
               types.InlineKeyboardButton('Назад', callback_data='back'))
    return markup7

from telebot import types

def mainMenu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Каталог', 'Информация')
    return markup


def catalog_choice():
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup1.row('Товар1', 'Товар2', 'Товар3', 'Товар4', 'Товар5')
    return markup1


def choice_markup():
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    markup2.add(types.InlineKeyboardButton('Информация', callback_data='info'),
                types.InlineKeyboardButton('Купить', callback_data='buy'))
    return markup2


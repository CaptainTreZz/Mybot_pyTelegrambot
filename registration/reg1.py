bot = telebot.TeleBot(TOKEN)


@bot.callback_query_handler(func=lambda call: True)
def add_user_name(call):
    msgname = bot.send_message(call.from_user.id, "Введите свое имя.")
    bot.register_next_step_handler(msgname, add_user_first)


def add_user_first(call):
    add_user_name()
    bot.send_message(call.from_user.id, "Отлично, я запомнил вас!")


def add_user_surname(call):
    msgsurname = bot.send_message(call.from_user.id, "Введите свою фамилию.")
    bot.register_next_step_handler(msgsurname, add_user_surname)


def add_user_last(call):
    add_user_surname()
    bot.send_message(call.from_user.id, "Отлично, я запомнил вас!")
import sqlite3

# Подключение базы данных в sqlite3
conn = sqlite3.connect('database/db_bot.db', check_same_thread=False)
cur = conn.cursor()


# Добавление пользователя в базу данных для обработки
def db_table_user(user_id: int, name: str):
    cur.execute('INSERT INTO users (user_id, name) '
                'VALUES (?, ?)', (user_id, name))
    conn.commit()


# Добавление в корзину товара
def db_table_product(id: int, title: str, content: str):
    pass

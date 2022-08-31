import sqlite3

# Подключение базы данных в sqlite3
conn = sqlite3.connect('database/db_bot.db', check_same_thread=False)
cur = conn.cursor()


# Добавление пользователя в базу данных для обработки
def db_table_val(user_id: int, name: str, surname: str):
    cur.execute("INSERT INTO users (user_id, name, surname) VALUES (?, ?, ?)", (user_id, name, surname))
    conn.commit()


def db_table_get(user_id: int, name: str, surname: str):
    cur.execute("SELECT * FROM users")
    conn.commit()

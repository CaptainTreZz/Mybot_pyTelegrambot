import sqlite3


try:
    conn = sqlite3.connect('database/db.db', check_same_thread=False)
    cursor = conn.cursor()
    print("Соединение с базой данных установлено.")

except sqlite3.DatabaseError as err:
    print("Error: ", err)

def add_user(user_id: int, first_name: str, last_name: str):
    if cursor.execute("INSERT INTO users (user_id, first_name, last_name) VALUES (?, ?, ?)",
                   (user_id, first_name, last_name)):
        conn.commit()
        conn.close()

# def check_user(first_name: str, last_name: str):
#     cursor.execute("SELECT first_name, last_name FROM users")
#     if cursor.fetchall() == main.message.from_user.first_name:
#         if cursor.fetchall() == main.message.from_user.last_name:
#             new_user = add_user(first_name=main.message.from_user.first_name, last_name=main.message.from_user.last_name)
#             return new_user
#     conn.commit()
#     conn.close()

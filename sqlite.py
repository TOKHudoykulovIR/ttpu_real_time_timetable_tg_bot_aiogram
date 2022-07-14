import sqlite3


def sql_start():
    print("checkpoint sql1")
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(id INTEGER , name MESSAGE_TEXT , text MESSAGE_TEXT , time TIMESTAMP )"""
    )
    connect.commit()
    cursor.close()


async def add_user(id, name, text, time):
    print("checkpoint sql2")
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (id, name, text, time))
    connect.commit()
    cursor.close()


async def get_info():
    print("checkpoint sql3")
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    return data

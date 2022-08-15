import csv
import sqlite3


def sql_start():
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(id INTEGER , name MESSAGE_TEXT , text MESSAGE_TEXT , time TIMESTAMP )"""
    )
    connect.commit()
    cursor.close()


async def add_user(id, name, text, time):
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users VALUES(?, ?, ?, ?)", (id, name, text, time))
    connect.commit()
    cursor.close()


async def get_info():
    connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM users")
    with open("usage_history.csv", "w", newline='') as csv_file:
        print('users history >>> converting')

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # write headers
        csv_writer.writerows(cursor)

        # data = cursor.fetchall()
        # cursor.close()
        # return data

    cursor.execute("SELECT id, name, count(*) as request_qty FROM users GROUP BY id")
    with open("users_list.csv", "w", newline='') as csv_file:
        print('users list >>> converting')

        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # write headers
        csv_writer.writerows(cursor)

    cursor.close()

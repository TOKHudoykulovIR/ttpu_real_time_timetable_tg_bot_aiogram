import os
import csv
# import sqlite3
import psycopg2


def sql_start():
    connect = psycopg2.connect(os.environ.get("DATABASE_URL"), sslmode="require")
    cursor = connect.cursor()

    # connect = sqlite3.connect("users.db")

    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users(id integer, name varchar , command varchar , time timestamp)"""
    )
    connect.commit()
    cursor.close()


async def add_user(id, name, command, time):
    connect = psycopg2.connect(os.environ.get("DATABASE_URL"), sslmode="require")
    # connect = sqlite3.connect("users.db")
    cursor = connect.cursor()
    cursor.execute("INSERT INTO users (id, name, command, time) VALUES(%s, %s, %s, %s)", (id, name, command, time))
    connect.commit()
    cursor.close()


async def get_info():
    connect = psycopg2.connect(os.environ.get("DATABASE_URL"), sslmode="require")
    # connect = sqlite3.connect("users.db")
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

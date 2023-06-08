import mysql.connector
from mysql.connector import Error
from os import environ
from dotenv import load_dotenv
import time

load_dotenv()


def connect():
    while True:
        try:
            mydb = mysql.connector.connect(
                port=3306,
                host=environ["db_host"],
                user=environ["db_user_login"],
                password=environ["db_user_password"],
                database=environ["db_name"],
            )

            if mydb.is_connected():
                print("Успешное подключение к базе данных MySQL")
                return mydb
        except Error as e:
            print(f"Ошибка подключения к базе данных MySQL: {e}")

            # Ждем перед следующей попыткой подключения
            time.sleep(5)

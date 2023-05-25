import mysql.connector
from os import environ
from dotenv import load_dotenv

load_dotenv()

def connect():
    mydb = mysql.connector.connect(
        port=3306,
        host=environ["db_host"],
        user=environ["db_user_login"],
        password=environ["db_user_password"],
        database="db"
    )
    return mydb

import mysql.connector
from os import environ
from dotenv import load_dotenv

load_dotenv()

def convert_data(file_name):
    with open(file_name, 'rb') as file:
        binary_data = file.read()
    return binary_data

def connect():
    mydb = mysql.connector.connect(
        port=3306,
        host="127.0.0.1",
        user=environ["db_user_login"],
        password=environ["db_user_password"],
        database="db"
    )
    return mydb


def select_all():
   return
def select_name():
    return

def select_project():
    return

def get_group():
    return

# docker - compose - f docker - compose.yaml up

# mycursor = mydb.cursor()
#
# sql = "DROP TABLE IF EXISTS medias "
#
# mycursor.execute(sql)
#
# mycursor.execute("CREATE TABLE IF NOT EXISTS medias (name_ VARCHAR(255), data_ MEDIUMBLOB)")
# sql = "INSERT INTO medias (name_, data_) VALUES (%s, %s)"
# name = 'test'
# data_file = convert_data('/Users/darja/PycharmProjects/DBProject/photo.jpg')
# mycursor.execute(sql, (name, data_file))
# mydb.commit()

# sql = "UPDATE medias SET data_=convert_data('/Users/darja/PycharmProjects/DBProject/photo.jpg') WHERE name_='test'"
# sql = "INSERT INTO medias (name, data) VALUES ('test', 'photo')"
# mycursor.execute(sql)
# mydb.commit()

# mycursor.execute("SELECT data_ FROM medias")
# myresult = mycursor.fetchall()
#
# import base64
#
# for x in myresult:
#     print(base64.b64encode(x[0]))

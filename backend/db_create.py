import mysql.connector
from os import environ


def convert_data(file_name):
    with open(file_name, 'rb') as file:
        binary_data = file.read()
    return binary_data


mydb = mysql.connector.connect(
  port=3306,
  host=environ["db_host"],
  user=environ["db_user_login"],
  password=environ["db_user_password"],
  database=environ["db_name"]
)
# docker - compose - f docker - compose.yaml up

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS group_list (group_uuid VARCHAR(36) DEFAULT (UUID()) NOT NULL PRIMARY KEY, group_ VARCHAR(100), group_year YEAR)")
mydb.commit()
mycursor.execute("CREATE TABLE IF NOT EXISTS type_list (type_uuid VARCHAR(36) DEFAULT (UUID()) NOT NULL PRIMARY KEY, type_ VARCHAR(100))")
mydb.commit()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS project_info (
  project_uuid int PRIMARY KEY NOT NULL AUTO_INCREMENT, 
  project_name VARCHAR(255),   
  group_uuid VARCHAR(36) DEFAULT (UUID()),
  year_ YEAR,
  type_uuid VARCHAR(36) DEFAULT (UUID()),
  is_best VARCHAR(4),
  CONSTRAINT FK_group_uuid FOREIGN KEY (group_uuid) REFERENCES group_list(group_uuid), 
  CONSTRAINT FK_type_uuid FOREIGN KEY (type_uuid) REFERENCES type_list(type_uuid)
)
""")
mycursor.execute('''CREATE TABLE IF NOT EXISTS students (
    student_uuid varchar(36) DEFAULT (UUID()) NOT NULL PRIMARY KEY, 
    first_name VARCHAR(100), 
    last_name VARCHAR(100),
    project_uuid int,
    CONSTRAINT FK_project_uuid FOREIGN KEY (project_uuid) REFERENCES project_info(project_uuid));
''')
mydb.commit()
mycursor.execute("""
CREATE TABLE IF NOT EXISTS files (
  project_uuid int, 
  pdf_file VARCHAR(300), 
  app_1 VARCHAR(300), 
  app_2 VARCHAR(300), 
  app_3 VARCHAR(300), 
  app_4 VARCHAR(300),
  app_5 VARCHAR(300),
  app_6 VARCHAR(300),
  app_7 VARCHAR(300),
  app_8 VARCHAR(300),
  app_9 VARCHAR(300),
  app_10 VARCHAR(300),
  app_11 VARCHAR(300), 
  app_12 VARCHAR(300), 
  app_13 VARCHAR(300), 
  app_14 VARCHAR(300),
  app_15 VARCHAR(300),
  app_16 VARCHAR(300),
  app_17 VARCHAR(300),
  app_18 VARCHAR(300),
  app_19 VARCHAR(300),
  app_20 VARCHAR(300),
  app_21 VARCHAR(300),
  app_22 VARCHAR(300),
  app_23 VARCHAR(300),
  app_24 VARCHAR(300),
  app_25 VARCHAR(300),
 CONSTRAINT FK_project_uuid_ FOREIGN KEY (project_uuid) REFERENCES project_info(project_uuid)
); 
""")

mydb.commit()
sql = '''ALTER TABLE project_info
ADD CONSTRAINT UC_Project UNIQUE (project_name,year_,group_uuid);'''
mycursor.execute(sql)
mydb.commit()

sql = '''ALTER TABLE group_list
ADD CONSTRAINT UC_Group UNIQUE (group_, group_year);'''
mycursor.execute(sql)
mydb.commit()

sql = '''ALTER TABLE type_list
ADD CONSTRAINT UC_Type UNIQUE (type_);'''
mycursor.execute(sql)
mydb.commit()

sql = '''ALTER TABLE students
ADD CONSTRAINT UC_Student UNIQUE (first_name, last_name, project_uuid);'''
mycursor.execute(sql)
mydb.commit()

print("done")

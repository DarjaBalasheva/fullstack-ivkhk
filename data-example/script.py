import os
from dotenv import load_dotenv
import json
import backend.db_connect

load_dotenv()


# def connect():  # Connect to DB
#     mydb = mysql.connector.connect(
#         port=3306,
#         host="127.0.0.1",
#         user=environ["db_user_login"],
#         password=environ["db_user_password"],
#         database="db",
#     )
#     return mydb
# mydb = connect()
mydb = backend.db_connect.connect()
mycursor = mydb.cursor()


YEAR_PATH = "./{year}/"
GROUP_PATH = "./{year}/{group}"
PROJECT_PATH = "./{year}/{group}/{project}"


for year_ in os.listdir("."):
    if os.path.isdir(year_):
        if year_[0] == ".":
            continue

        for group in os.listdir(YEAR_PATH.format(year=year_)):
            if os.path.isdir(GROUP_PATH.format(year=year_, group=group)):
                if group != "inspectionProfiles":
                    sql = f"""INSERT IGNORE INTO group_list (
                        group_year, group_)
                        VALUES (%s, %s);"""
                    mycursor.execute(sql, (year_, group))
                    group_id = mycursor.lastrowid
                    mydb.commit()
                    if group_id == 0:  # Group already exist
                        sql = f"""SELECT group_uuid FROM group_list WHERE
                                group_year=%s
                                AND group_=%s"""

                        mycursor.execute(sql, (year_, group))
                        group_id = mycursor.fetchall()[0][0]

                for project in os.listdir(GROUP_PATH.format(year=year_, group=group)):
                    if (
                        os.path.isdir(
                            PROJECT_PATH.format(
                                year=year_, group=group, project=project
                            )
                        )
                        and project[0] != "."
                    ):
                        with open(
                            f"""{PROJECT_PATH.format(year=year_,
                                                     group=group,
                                                     project=project)}/prop.json""",
                            "r",
                        ) as file:
                            info = json.load(file)
                            # bb = aa.replace('\n', ';').split(sep=';')
                            # print(bb)
                            project_type = info["type"]
                        sql = f"""INSERT IGNORE INTO type_list (type_)
                                    VALUES (%s);"""
                        mycursor.execute(sql, (project_type,))
                        type_id = mycursor.lastrowid
                        mydb.commit()
                        if type_id == 0:  # type project already exist
                            sql = f"""SELECT type_uuid FROM type_list WHERE 
                                    type_=%s"""
                            mycursor.execute(sql, (project_type,))
                            type_id = mycursor.fetchall()[0][0]
                            mydb.commit()

                        is_best = info["best"]

                        sql = f"""INSERT IGNORE INTO project_info (
                        project_name,
                        year_,
                        group_uuid,
                        type_uuid,
                        is_best) 
                        VALUES (%s, %s , %s, %s, %s);"""
                        mycursor.execute(
                            sql, (project, year_, group_id, type_id, is_best)
                        )
                        project_id = mycursor.lastrowid

                        mydb.commit()
                        # print(project_id)

                        if project_id == 0:  # project already exist
                            sql = f"""SELECT * FROM project_info WHERE 
                             project_name=%s AND year_=%s"""
                            mycursor.execute(sql, (project, year_))
                            project_id = mycursor.fetchall()[0][0]
                            mydb.commit()
                            continue  # File already exist. Cycle end

                        for name in info["name"]:
                            student_first_name_, student_last_name_ = name.split()
                            print(f"First name: {student_first_name_}")
                            print(f"Last name: {student_last_name_}")

                            sql = f"""INSERT IGNORE INTO students (
                            first_name,
                            last_name,
                            project_uuid)
                            VALUES (%s, %s, %s);"""
                            mycursor.execute(
                                sql,
                                (student_first_name_, student_last_name_, project_id),
                            )
                            mydb.commit()

                        # path = path + project + '/'
                        files_dict_for_insert = {
                            "media_file": [],
                            "project_file": [],
                            "archive": [],
                            "others": [],
                        }
                        for media_type in os.listdir(
                            f"""{PROJECT_PATH.format(year=year_,
                                                     group=group,
                                                     project=project)}/"""
                        ):
                            if (
                                os.path.isdir(
                                    f"""{PROJECT_PATH.format(year=year_,
                                                             group=group,
                                                             project=project)}/{media_type}"""
                                )
                                and media_type[0] != "."
                            ):
                                for file in os.listdir(
                                    f"""{PROJECT_PATH.format(year=year_,
                                                            group=group,
                                                            project=project)}/{media_type}"""
                                ):
                                    if file[0] != ".":
                                        files_dict_for_insert[media_type].append(
                                            os.path.abspath(
                                                f"""{PROJECT_PATH.format(year=year_,
                                                                         group=group,
                                                                         project=project)}/{media_type}/{file}"""
                                            )
                                        )
                                        print(
                                            "!!!!!!!!",
                                            len(files_dict_for_insert["media_file"]),
                                        )
                        if len(files_dict_for_insert["media_file"]) == 0:
                            files_dict_for_insert["media_file"].append(
                                "/Users/darja/script/nofile.png"
                            )
                        if len(files_dict_for_insert["project_file"]) == 0:
                            files_dict_for_insert["project_file"].append(
                                "/Users/darja/script/nofile.png"
                            )
                        app_columns = ",".join(
                            [
                                f"app_{i+1}"
                                for i in range(len(files_dict_for_insert["media_file"]))
                            ]
                        )
                        app_values = [_ for _ in files_dict_for_insert["media_file"]]
                        app_values.append(files_dict_for_insert["project_file"][0])
                        app_values.append(project_id)

                        sql = f"""INSERT IGNORE INTO files (
                        {app_columns},
                        pdf_file,
                        project_uuid)
                        VALUES {tuple(_ for _ in app_values)};
                        """
                        print(sql)
                        mycursor.execute(sql)
                        mydb.commit()

print("done")

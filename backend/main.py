from typing import Union

from data import students_dict, domen, key_search

from fastapi import FastAPI, Request, Query, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from functions import *
from db_connect import connect



app = FastAPI()
app.db = connect()

app.mount("/static", StaticFiles(directory="../static"), name="static")

app.mount("/Users", StaticFiles(directory="/Users"), name="media")

templates = Jinja2Templates(directory="../templates")


@app.get("/home", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Multimedia projects"})



@app.get("/result", response_class=HTMLResponse)
async def read_items(request: Request, message: Union[str, None] = Query(default=None), key: Union[str, None] = Query(default=None)):
    conn = request.app.db
    cursor = conn.cursor()
    cursor = conn.cursor(dictionary=True)
    message = message.lower()
    if message and key:
        if key == 'all':
            try:
                sql = f'''SELECT  project_info.project_uuid, project_info.project_name, project_info.year_, 
                type_list.type_, group_list.group_, students.first_name, students.last_name, students.student_uuid

                FROM project_info

                JOIN type_list ON type_list.type_uuid = project_info.type_uuid
                JOIN group_list ON group_list.group_uuid = project_info.group_uuid
                JOIN students ON students.project_uuid = project_info.project_uuid

                WHERE LOWER(group_) LIKE %s
                    OR LOWER(year_) LIKE %s
                    OR LOWER(type_) LIKE %s
                    OR LOWER(first_name) LIKE %s 
                    OR LOWER(last_name) LIKE %s 
                    OR CONCAT(LOWER(first_name), ' ', LOWER(last_name)) LIKE %s 
                    OR CONCAT(LOWER(last_name), ' ', LOWER(first_name)) LIKE %s'''
                cursor.execute(sql, (message + '%', message + '%', message + '%', message + '%', message + '%', '%' + message, '%' + message + '%'))
                result = dict_create(cursor.fetchall())
            except KeyError:
                return templates.TemplateResponse("notFound.html",
                                                  {
                                                      "request": request,
                                                      "title": "Not Found",
                                                  },
                                                  status_code=404)
        elif key == 'top':
            sql = f'''SELECT  project_info.project_uuid, project_info.project_name, project_info.year_, project_info.is_best,
                type_list.type_, group_list.group_, students.first_name, students.last_name, students.student_uuid

                FROM project_info

                JOIN type_list ON type_list.type_uuid = project_info.type_uuid
                JOIN group_list ON group_list.group_uuid = project_info.group_uuid
                JOIN students ON students.project_uuid = project_info.project_uuid

                WHERE LOWER(group_) LIKE %s
                    OR LOWER(year_) LIKE %s
                    OR LOWER(type_) LIKE %s
                    OR LOWER(first_name) LIKE %s 
                    OR LOWER(last_name) LIKE %s 
                    OR CONCAT(LOWER(first_name), ' ', LOWER(last_name) LIKE %s 
                    OR CONCAT(LOWER(last_name), ' ', LOWER(first_name)) LIKE %s)
                    AND is_best = 1'''
            cursor.execute(sql, (message + '%', message + '%', message + '%', message + '%', message + '%', '%' + message, '%' + message + '%'))
            result = dict_create(cursor.fetchall())
        elif key == 'name':
            try:
                message
                sql = f'''SELECT project_info.project_uuid, project_info.project_name, project_info.year_, 
                type_list.type_, group_list.group_, students.*

                FROM project_info

                JOIN type_list ON type_list.type_uuid = project_info.type_uuid
                JOIN group_list ON group_list.group_uuid = project_info.group_uuid
                JOIN students ON students.project_uuid = project_info.project_uuid

                WHERE LOWER(first_name) LIKE %s 
                OR LOWER(last_name) LIKE %s 
                OR CONCAT(LOWER(first_name), ' ', LOWER(last_name)) LIKE %s 
                OR CONCAT(LOWER(last_name), ' ', LOWER(first_name)) LIKE %s'''
                cursor.execute(sql, (message + '%', message + '%', '%' + message, '%' + message + '%'))
                result = dict_create(cursor.fetchall())

            except KeyError:
                return templates.TemplateResponse("notFound.html",
                                                  {
                                                      "request": request,
                                                      "title": "Not Found",
                                                  },
                                                  status_code=404)
        else:
            try:
                sql = f'''SELECT   project_info.project_name, project_info.year_, 
                type_list.type_, group_list.group_, students.first_name, students.last_name, students.student_uuid
                
                FROM project_info
                
                JOIN type_list ON type_list.type_uuid = project_info.type_uuid
                JOIN group_list ON group_list.group_uuid = project_info.group_uuid
                JOIN students ON students.project_uuid = project_info.project_uuid
                
                WHERE LOWER({key}) LIKE %s '''
                cursor.execute(sql, (message+'%',))
                result = dict_create(cursor.fetchall())
                print(result)

            except KeyError:
                return templates.TemplateResponse("notFound.html",
                    {
                        "request": request,
                        "title": "Not Found",
                    },
                status_code=404)


    elif key == 'top' and not message:
        sql = f'''SELECT  project_info.project_uuid, project_info.project_name, project_info.year_, project_info.is_best,
                        type_list.type_, group_list.group_, students.first_name, students.last_name, students.student_uuid

                        FROM project_info

                        JOIN type_list ON type_list.type_uuid = project_info.type_uuid
                        JOIN group_list ON group_list.group_uuid = project_info.group_uuid
                        JOIN students ON students.project_uuid = project_info.project_uuid

                        WHERE is_best = 1'''
        cursor.execute(sql)
        result = dict_create(cursor.fetchall())
        print(result)
    elif not message:
        sql = f'''SELECT  students.student_uuid, project_info.project_name, project_info.year_, 
                            type_list.type_, group_list.group_, students.first_name, students.last_name FROM
                                   project_info 
        JOIN type_list ON type_list.type_uuid = project_info.type_uuid
        JOIN group_list ON group_list.group_uuid = project_info.group_uuid
        JOIN students ON students.project_uuid = project_info.project_uuid'''

        cursor.execute(sql)
        result = dict_create(cursor.fetchall())

    if not result:
        return templates.TemplateResponse("notResult.html", {
            "request": request,
            "server": domen,
            "title": "Not Result",
        },
    )

    else:
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "server": domen,
                "results": result,
                "title": "Result",
            },
        )

@app.get("/result", response_class=HTMLResponse, status_code=500)
async def response_page(request: Request, message: Union[str, None] = Query(default=None), key: Union[str, None] = Query(default=None)):
    return templates.TemplateResponse("notResult.html", {
            "request": request})

@app.get("/project", response_class=HTMLResponse)
async def project_page(
    request: Request,
    project: Union[str, None] = Query(default=None),
    uuid: Union[str, None] = Query(default=None),
):
    conn = request.app.db
    cursor = conn.cursor(dictionary=True)

    sql = f'''SELECT project_info.project_uuid, students.student_uuid, project_info.project_name, project_info.year_, 
                    type_list.type_, group_list.group_, students.first_name, students.last_name,
                    files.*
                    FROM project_info 
                        JOIN type_list ON type_list.type_uuid = project_info.type_uuid
                        JOIN group_list ON group_list.group_uuid = project_info.group_uuid
                        JOIN students ON students.project_uuid = project_info.project_uuid
                        JOIN files ON files.project_uuid = project_info.project_uuid
            WHERE students.student_uuid = %s'''
    if project and uuid:
        try:
            cursor.execute(sql, (uuid,))
            result = dict_create(cursor.fetchall())[0]
            print(result)
            medias = create_media_list(result)
            print('******', medias)

        except KeyError:
            return templates.TemplateResponse("notFound.html",
                        {
                            "request": request,
                            "title": "Not Found",
                        },
                    status_code=404)
        except IndexError:
            return templates.TemplateResponse("notFound.html",
                                              {
                                                  "request": request,
                                                  "title": "Not Found",
                                              },
                                              status_code=404)

    if not result:
        return templates.TemplateResponse("notFound.html",

                        {
                            "request": request,
                            "title": "Not Found",
                        },
                    status_code=404)
    else:
        return templates.TemplateResponse(
            "project.html",
            {"request": request, "result": result, "medias": medias, "title": "Project page"},
        )


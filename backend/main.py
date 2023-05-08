from typing import Union

from data import students_dict, domen, key_search

from fastapi import FastAPI, Request, Query, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from functions import *
from db_connect import connect
import base64



app = FastAPI()
app.db = connect()

app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../templates")


@app.get("/home", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Multimedia projects"})



@app.get("/result", response_class=HTMLResponse)
async def read_items(request: Request, message: Union[str, None] = Query(default=None), key: Union[str, None] = Query(default=None)):
    conn = request.app.db
    cursor = conn.cursor()
    if message:
        if key:
            if key == 'all':
                # cursor.execute("SELECT * FROM medias")
                result = find_everyone(students_dict, message)
            elif key == 'top':
                result = find_better(students_dict, message)
            else:
                try:
                    sql = f'''SELECT  project_info.project_uuid, project_info.project_name, project_info.year_, 
                    type_list.type_, group_list.group_, students.first_name, students.last_name FROM
                           project_info 
JOIN type_list ON type_list.type_uuid = project_info.type_uuid
JOIN group_list ON group_list.group_uuid = project_info.group_uuid
JOIN students ON students.project_uuid = project_info.project_uuid
                    WHERE {key} = %s'''
                    cursor.execute(sql, (message,))
                    result = dict_create(cursor.fetchall())
                except KeyError:
                    return templates.TemplateResponse("notFound.html",
                        {
                            "request": request,
                            "title": "Not Found",
                        },
                    status_code=404)
    else:
            if key == 'top':
                result = find_all_better(students_dict)
            else:
                sql = f'''SELECT  project_info.project_uuid, project_info.project_name, project_info.year_, 
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
    if project and uuid:
        result = find_project(students_dict, uuid)
        if not result:
            return templates.TemplateResponse("notFound.html",
                        {
                            "request": request,
                            "title": "Not Found",
                        },
                    status_code=404)
        return templates.TemplateResponse(
            "project.html",
            {"request": request, "result": result, "title": "Project page"},
        )
    return templates.TemplateResponse("notFound.html",
                        {
                            "request": request,
                            "title": "Not Found",
                        },
                    status_code=404)

@app.get("/db", response_class=HTMLResponse)
def home(request: Request):
    conn = request.app.db
    cursor = conn.cursor()
    cursor.execute("SELECT data_ FROM medias")
    img_result: tuple = cursor.fetchone()
    img_result: bytes = base64.b64encode(img_result[0])
    img_result: str = img_result.decode('utf-8')

    return templates.TemplateResponse("img.html", {
                "request": request,
                "app_file_primary": img_result})
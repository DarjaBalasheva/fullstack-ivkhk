from typing import Union

from data import students_dict, domen,key_search

from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from functions import find_everyone, find_all, find_project, find_item


app = FastAPI()


project_img = "../static/img/project_mg/project2.jpeg"
app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../templates")

@app.get("/home", response_class=HTMLResponse)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Multimedia projects"})



@app.get("/result", response_class=HTMLResponse)
async def read_items(request: Request, message: Union[str, None] = Query(default=None), key: Union[str, None] = Query(default=None)):
    if message:
        if key:
            if key == 'kõik':
                result = find_everyone(students_dict, message)
            elif key == 'paremik':
                result == find_everyone(students_dict, message)
            else:
                result = find_item(students_dict, key, message)
    else:
        result = find_all(students_dict)["data"]
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "server": domen,
            "results": result,
            "title": "Result",
        },
    )


@app.get("/project", response_class=HTMLResponse)
async def project_page(
    request: Request,
    project: Union[str, None] = Query(default=None),
    uuid: Union[str, None] = Query(default=None),
):
    if project and uuid:
        result = find_project(students_dict, uuid)
        return templates.TemplateResponse(
            "project.html",
            {"request": request, "result": result, "title": "Project page"},
        )
    return 404

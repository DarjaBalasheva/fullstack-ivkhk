from typing import Union

from data import students_dict, domen, key_search

from fastapi import FastAPI, Request, Query, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from functions import *



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
            elif key == 'top':
                result = find_better(students_dict, message)
            else:
                try:
                    result = find_item(students_dict, key, message)
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
                result = find_all(students_dict)["data"]
    
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

from typing import Union

from fastapi import FastAPI, Request, Query, Body
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from functions import find_everyone, find_all, find_item
from data import students_dict

app = FastAPI()

app.mount("/static", StaticFiles(directory="../static"), name="static")
templates = Jinja2Templates(directory="../templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
	return templates.TemplateResponse("index.html",{"request":request})

@app.get("/result", response_class=HTMLResponse)
async def read_items(request: Request, message: Union[str, None] = Query(default=None)):
    if message:
          result = find_item(students_dict, 'name', message)
    else:
          result = find_all(students_dict)["data"]
    return templates.TemplateResponse("result.html",{"request":request,
                                                     "results": result})


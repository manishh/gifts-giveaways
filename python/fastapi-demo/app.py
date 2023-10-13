from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from books import get_books_data

# https://fastapi.tiangolo.com/
# https://fastapi.tiangolo.com/advanced/templates/

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


class CurrencyData(BaseModel):
    price: float
    currency: str


@app.get("/")
def read_root():
    return {"What's Up": "Testing FastAPI/Uvicorn"}


@app.get("/books-api")
def get_book_api(q: Union[str, None] = None):
    return get_books_data(q)


@app.get("/books", response_class=HTMLResponse)
def get_books(request: Request, q: Union[str, None] = None):
    books = get_books_data(q)
    return templates.TemplateResponse("books.html", {"request": request, "books_list": books, "q": q})

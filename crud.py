from fastapi import FastAPI,status
from pydantic  import BaseModel
from fastapi.exceptions import HTTPException

books  = [

    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Smith",
        "publish_date": "2020-01-15"
    },
    {
        "id": 2,
        "title": "Mastering FastAPI",
        "author": "Alice Johnson",
        "publish_date": "2021-03-20"
    },
    {
        "id": 3,
        "title": "Django in Action",
        "author": "Robert Brown",
        "publish_date": "2019-07-10"
    },
    {
        "id": 4,
        "title": "REST API Design",
        "author": "Emily Davis",
        "publish_date": "2022-05-12"
    },
    {
        "id": 5,
        "title": "Learning SQL",
        "author": "Michael Wilson",
        "publish_date": "2018-11-01"
    },
    {
        "id": 6,
        "title": "JavaScript Essentials",
        "author": "Sophia Taylor",
        "publish_date": "2021-09-18"
    },
    {
        "id": 7,
        "title": "React for Beginners",
        "author": "Daniel Anderson",
        "publish_date": "2023-02-28"
    },
    {
        "id": 8,
        "title": "Microservices Architecture",
        "author": "Olivia Thomas",
        "publish_date": "2020-08-05"
    },
    {
        "id": 9,
        "title": "Cloud Computing Guide",
        "author": "William Martin",
        "publish_date": "2022-12-15"
    },
    {
        "id": 10,
        "title": "Data Structures with Python",
        "author": "Emma White",
        "publish_date": "2019-04-22"
    }
]

app = FastAPI()

@app.get("/books")

def get_books():
    return books

@app.get("/book/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book_id == book["id"]:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book doesnt exit")

class Book(BaseModel):
    id:int
    title:str
    author:str
    publish_date:str

@app.post("/book")

def create_book(book:Book):
    new_book = book.model_dump()
    books.append(new_book)

class Book_update(BaseModel):
    title:str
    author:str
    publish_date:str 

@app.put("/book/{book_id}")
def update_book(book_id:int,book_update:Book_update):
    for book in books:
        if book_id == book["id"]:
            book["title"] = book_update.title
            book["author"] = book_update.author
            book["publish_date"] = book_update.publish_date
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Data not found")



@app.delete("/book/{book_id}")
def delete_book(book_id:int):
    for book in books:
        if book_id == book["id"]:
            books.remove(book)
            return {"msg":"Book deleted sucessfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book doesnt exit")
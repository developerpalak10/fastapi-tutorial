from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

app = FastAPI()

@app.get("/")

def read_root():
    return {"Hello":"11"}


@app.get("/greet")

def greet():
    return {"name":"Hello sam"}

@app.get("/greet/{name}")

def greet_name(name:str,age:Optional[int]=None):
    return {"message":f"Hello {name} and age is {age}"}



class Student(BaseModel):
    name:str
    age:int
    roll:int


@app.post("/create_student")

def create_student(student:Student):
    return {
        "name":student.name,
        "age":student.age,
        "roll":student.roll

    }




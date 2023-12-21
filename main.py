#API to add people and their info to a database as well as retrieve the info

from email.policy import HTTP
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
app = FastAPI()


data = [{"name": "name of person", "age": "age of person", "gender": "gender of person", "id": "0"}, 
        {"name": "Ahmed Amrou", "age": "20", "gender": "male", "id": "1"},
        {"name": "Robert Stevens", "age": "64", "gender": "male", "id": "2"}]


def find_name(id):
    for p in data:
        if p["id"] == id:
            return str(p)

        
def find_index_name(id):
    for i, p in enumerate(data):
        if p["id"] == id:
            return str(i)


class Person(BaseModel):
    name: str
    age: int
    gender: str
    id: Optional[int] = None

@app.get("/")
def root():
    return "Frontpage"

@app.get("/people")
def view_people():
    return {"data": data}

@app.post("/people", status_code=status.HTTP_201_CREATED)
def add_person(new_person: Person):
    new_person_dict = new_person.dict()
    new_person_dict["id"] = randrange(1, 1000000000)
    return new_person_dict

@app.get("/people/{id}")
def view_person(id: int):
    post = find_name(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@app.delete("/people/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(id):
    post_index = find_index_name(id)
    if not post_index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    data.pop(int(post_index))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
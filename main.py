#API to add people and their info to a database as well as retrieve the info

from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel
from random import randrange
app = FastAPI()


data = [{"name": "name of person", "age": "age of person", "gender": "gender of person", "id": "1"}, {"name": "Ahmed Amrou", "age": "20", "gender": "male", "id": "1"}]


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

@app.post("/people")
def add_person(new_person: Person):
    new_person_dict = new_person.dict()
    new_person_dict["id"] = randrange(1, 1000000000)
    return new_person_dict
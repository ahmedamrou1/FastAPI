#API to add people and their info to a database as well as retrieve the info


import models
from database import engine, get_db
from email.policy import HTTP
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session

app = FastAPI()




while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'password123', cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database successfully connected")
        break
    except Exception as error:
        print(f"Error connecting to database: {error}")
        time.sleep(2)


class Person(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    gender: Optional[str]
    email: str
    phone_number: Optional[str]

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return "Frontpage"

@app.get("/people")
def test_posts(db: Session = Depends(get_db)):
    people = db.query(models.Person).all()
    return people

@app.post("/people", status_code=status.HTTP_201_CREATED)
def add_person(person: Person, db: Session = Depends(get_db)):
   
   new_person = models.Person(**person.model_dump())
   db.add(new_person)
   db.commit()
   db.refresh(new_person)
   return new_person

@app.get("/people/{id}")
def view_person(id: str): 
    cursor.execute("""SELECT * FROM people WHERE id = %s""", (str(id),))   
    person = cursor.fetchone()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    return person
    

@app.delete("/people/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(id: str):
    cursor.execute("""DELETE FROM people WHERE id = %s RETURNING *""", (str(id),))
    person = cursor.fetchone()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    conn.commit()
    print("Post sucessfully deleted")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/people/{id}", status_code= status.HTTP_205_RESET_CONTENT)
def update_person(id: str, new_content: Person):
    cursor.execute("""UPDATE people SET first_name = %s, last_name = %s, gender = %s, birthday = %s, email = %s, phone_number = %s WHERE id = %s RETURNING *""", (new_content.first_name, new_content.last_name, new_content.gender, new_content.birthday, new_content.birthday, new_content.phone_number, str(id)))
    conn.commit()
    person = cursor.fetchone()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    return person


#5:15:56
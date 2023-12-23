#API to add people and their info to a database as well as retrieve the info

from email.policy import HTTP
from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

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

@app.get("/")
def root():
    return "Frontpage"

@app.get("/people")
def view_people():
    cursor.execute("""SELECT * FROM people;""")
    people = cursor.fetchall()
    return people

@app.post("/people", status_code=status.HTTP_201_CREATED)
def add_person(person: Person):
    cursor.execute("""INSERT INTO people (first_name, last_name, birthday, gender, email, phone_number) VALUES (%s, %s, %s, %s, %s, %s) RETURNING * """,(person.first_name, person.last_name, person.birthday, person.gender, person.email, person.phone_number))
    new_person = cursor.fetchone()
    conn.commit()
    return new_person

@app.get("/people/{id}")
def view_person(id: str):
    try: 
        cursor.execute("""SELECT * FROM people WHERE id = %s""", (str(id)))   
        return cursor.fetchone()
    except TypeError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    except psycopg2.errors.InvalidTextRepresentation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    

@app.delete("/people/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(id: str):
    try:
        cursor.execute("""DELETE FROM people WHERE id = %s""", (str(id),))
        cursor.fetchone()
        conn.commit()
        print("Post sucessfully deleted")
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except (psycopg2.ProgrammingError, psycopg2.errors.InvalidTextRepresentation):
        cursor.execute("ROLLBACK")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")

@app.put("/people/{id}", status_code= status.HTTP_205_RESET_CONTENT)
def update_person(id: int, new_content: Person):
    cursor.execute("""UPDATE people SET first_name = %s, last_name = %s, birthday = %s, gender = %s, email = %s, phone_number = %s RETURNING * """, (new_content.first_name, new_content.last_name, new_content.birthday, new_content.birthday, new_content.phone_number))
    updated = cursor.fetchone()
    return updated
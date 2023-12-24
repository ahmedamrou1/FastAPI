#API to add people and their info to a database as well as retrieve the info


import models, schemas
from database import engine, get_db
from email.policy import HTTP
from typing import Optional, List
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




models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return "Frontpage"

@app.get("/people", response_model=List[schemas.Person])
def test_posts(db: Session = Depends(get_db)):
    people = db.query(models.Person).all()
    return people

@app.post("/people", status_code=status.HTTP_201_CREATED, response_model=schemas.Person)
def add_person(person: schemas.CreatePerson, db: Session = Depends(get_db)):
   
   new_person = models.Person(**person.model_dump())
   db.add(new_person)
   db.commit()
   db.refresh(new_person)
   return new_person

@app.get("/people/{id}", response_model=schemas.PersonResponse)
def view_person(id: str,db: Session = Depends(get_db)): 
    result = db.query(models.Person).filter(models.Person.id == id).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    return result
    

@app.delete("/people/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_person(id: str, db: Session = Depends(get_db)):
    result = db.query(models.Person).filter(models.Person.id == id)
    if not result.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    result.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/people/{id}", status_code= status.HTTP_205_RESET_CONTENT, response_model=schemas.PersonResponse)
def update_person(id: str, new_content: schemas.UpdatePerson,db: Session = Depends(get_db)):
    query = db.query(models.Person).filter(models.Person.id == id)
    person = query.first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid post id")
    query.update(new_content.model_dump(), synchronize_session=False)
    db.commit()
    person = query.first()
    return person
    


#5:15:56
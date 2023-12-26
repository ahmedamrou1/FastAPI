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
import utils
import routers.people, routers.users, routers.auth

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = 'password123', cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database successfully connected")
        break
    except Exception as error:
        print(f"Error connecting to database: {error}")
        time.sleep(2)


app.include_router(routers.people.router)
app.include_router(routers.users.router)
app.include_router(routers.auth.router)

@app.get("/")
def root():
    return "Frontpage"


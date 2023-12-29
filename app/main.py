#API to add people and their info to a database as well as retrieve the info
from pydantic_settings import BaseSettings
import models
from database import engine
from fastapi import FastAPI
import routers.people, routers.users, routers.auth





app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(routers.people.router)
app.include_router(routers.users.router)
app.include_router(routers.auth.router)

@app.get("/")
def root():
    return "Frontpage"


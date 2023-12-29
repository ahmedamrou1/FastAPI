#API to add people and their info to a database as well as retrieve the info
from fastapi import FastAPI
import routers.people, routers.users, routers.auth
from fastapi.middleware.cors import CORSMiddleware



origins=["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.people.router)
app.include_router(routers.users.router)
app.include_router(routers.auth.router)

@app.get("/")
def root():
    return "Frontpage"


from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from .routers import post, user, auth
from .database import engine

import time
from . import models, schemas, utils


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi',
                                user='postgres', password='9997', cursor_factory=RealDictCursor)  # For Database Connection
        cursor = conn.cursor()  # execute sequel statement
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to database faied")
        print("Error: ", error)
        time.sleep(2)

my_posts = [{"title": "title of post 1", "content": "content of post", "id": 1}, {
    "title": "favorite foods", "content": "I like Pizza", "id": 2}]


def find_posts(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def root():
    return {"message": "Welcome to myAPI !!!"}

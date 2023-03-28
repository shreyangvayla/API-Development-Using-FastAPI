from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# request get method url get with: "/"


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/posts")
def get_posts():
    return {"data": "this is your post"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title {payload['title']} content: {payload['content']}"}

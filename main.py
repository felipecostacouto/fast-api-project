from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1","id": 1}, {"title":
"favorite foods", "content":"I like pizza","id":2}]   

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id" : item_id}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post():
    return {"data": "get single post"}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 100000000)
    my_posts.append(post_dict)
    return {"data": "post_dict"}
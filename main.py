from fastapi import FastApi
from pydantic import BaseModel
from typing import Union


app = FastApi()

class User(BaseModel):
    id: int
    email: str
    password: str

@app.get("/items/{user}")
def read_item(user: int, q: Union[str, None] = None):
    return {"user": user, "id":5,"email": "sam@gamil.com", "password":"password125Test"}

@app.put("/items/{user}")
def read_item(user: int, q: Union[str, None] = None):
    return {"user": user, "id":5,"email": "sam@gamil.com", "password":"password125Test"}


import fastapi 
from pydantic import BaseModel
from typing import Union

app = fastapi.FastAPI()

class User(BaseModel):
    id: int
    email: str
    password: str  

@app.get("/items/{user}")
def read_item(user: int, q: Union[str, None] = None):
    return {"user": user, "id": 5, "email": "sam@gmail.com"}

@app.put("/items/{user}")
def update_item(user: int, q: Union[str, None] = None):
    return {"message": "User updated successfully"}
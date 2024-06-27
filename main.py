import fastapi 
from pydantic import BaseModel
from typing import Union

app = fastapi.FastAPI()

class User(BaseModel):
    id: int
    email: str
    password: str  

@app.get("/items/{user}")
def read_item(user: int, id : int, email : str,):
    return {"user": user, "id": id, "email": email}

@app.put("/items/{user}")
def update_item(user: int, id : int, email : str,):
    return {"message": "User updated successfully"}

@app.delete("/items/{user}")
def delete_item(id : int):
    return {"message": "User deleted"}
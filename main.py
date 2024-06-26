from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    iduser: int
    email: str
    password: str

class Portefolio(BaseModel):
    id_portefolio: int
    id_user: int
    date: str
    price: float
    in_or_out: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Welcome"}


@app.get("/user/{id_user}")
def read_item(id_user: int, q: Union[str, None] = None):
    return {"id_user": id_user,
            "user_email": User.email,
            "q": q}


@app.put("/user/{id_user}")
def update_item(id_user: int, user: User):
    return {
            "user_email": User.email,
            "id_user": id_user
            }

#__

@app.get("/portefolio/{id_portefolio}")
def read_item(id_portefolio: int, q: Union[str, None] = None):
    return {"id_portefolio": Portefolio.id_portefolio,
            "price": Portefolio.price,
            "date": Portefolio.date,
            "in_or_out": Portefolio.in_or_out,
            }


@app.put("/portefolio/{id_portefolio}")
def update_item(id_user: int, user: User):
    return {"user_email": User.email, "id_user": id_user}
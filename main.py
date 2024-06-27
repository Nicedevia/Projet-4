import logging
from typing import Union, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

users_db = []
portefolio_db = []

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome"}

@app.post("/user/", response_model=User)
def create_user(user: User):
    users_db.append(user)
    logger.info(f"User created: {user}")
    return user

@app.get("/user/{id_user}", response_model=User)
def read_user(id_user: int):
    for user in users_db:
        if user.iduser == id_user:
            logger.info(f"User retrieved: {user}")
            return user
    logger.error(f"User not found: {id_user}")
    raise HTTPException(status_code=404, detail="User not found")

@app.put("/user/{id_user}", response_model=User)
def update_user(id_user: int, user: User):
    for idx, u in enumerate(users_db):
        if u.iduser == id_user:
            users_db[idx] = user
            logger.info(f"User updated: {user}")
            return user
    logger.error(f"User not found: {id_user}")
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{id_user}")
def delete_user(id_user: int):
    for idx, u in enumerate(users_db):
        if u.iduser == id_user:
            del users_db[idx]
            logger.info(f"User deleted: {id_user}")
            return {"message": "User deleted"}
    logger.error(f"User not found: {id_user}")
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/portefolio/", response_model=Portefolio)
def create_portefolio(portefolio: Portefolio):
    portefolio_db.append(portefolio)
    logger.info(f"Portefolio created: {portefolio}")
    return portefolio

@app.get("/portefolio/{id_portefolio}", response_model=Portefolio)
def read_portefolio(id_portefolio: int):
    for portefolio in portefolio_db:
        if portefolio.id_portefolio == id_portefolio:
            logger.info(f"Portefolio retrieved: {portefolio}")
            return portefolio
    logger.error(f"Portefolio not found: {id_portefolio}")
    raise HTTPException(status_code=404, detail="Portefolio not found")

@app.put("/portefolio/{id_portefolio}", response_model=Portefolio)
def update_portefolio(id_portefolio: int, portefolio: Portefolio):
    for idx, p in enumerate(portefolio_db):
        if p.id_portefolio == id_portefolio:
            portefolio_db[idx] = portefolio
            logger.info(f"Portefolio updated: {portefolio}")
            return portefolio
    logger.error(f"Portefolio not found: {id_portefolio}")
    raise HTTPException(status_code=404, detail="Portefolio not found")

@app.delete("/portefolio/{id_portefolio}")
def delete_portefolio(id_portefolio: int):
    for idx, p in enumerate(portefolio_db):
        if p.id_portefolio == id_portefolio:
            del portefolio_db[idx]
            logger.info(f"Portefolio deleted: {id_portefolio}")
            return {"message": "Portefolio deleted"}
    logger.error(f"Portefolio not found: {id_portefolio}")
    raise HTTPException(status_code=404, detail="Portefolio not found")

# Usable by frontend routes

@app.get("/get-from-api")
def streamlite():
    """Get from API

    This method is a sort of template of an endpoint used by the streamlit frontend.

    Nothing changes from the other routes, but the json sent will be used, thus the keys must be consistant.

    Here, the \"response\" key is used, whatever is for text, list, or dict.

    """

    return {"response": "this is a message from api"}

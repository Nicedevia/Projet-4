from fastapi import FastAPI
from database.connextion import engine, Base
from project.authroute.routes import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth")

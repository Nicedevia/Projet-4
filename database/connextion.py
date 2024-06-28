from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


try:
    with engine.connect() as conn:
        print("Connected to the database.")
except Exception as e:
    print(f"Unable to connect to the database: {e}")
    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

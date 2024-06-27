import logging
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from datetime import date
from database.connextion import get_db
from project.models import models

router = APIRouter()
logger = logging.getLogger(__name__)

class UserCreate(BaseModel):
    email: str
    password: str

class PortfolioCreate(BaseModel):
    user_id: int
    category: str
    date: str  # Note: This will be converted to a date object
    price: float
    description: str = None

@router.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = models.User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logger.info(f"User created: email='{user.email}'")
    return new_user

@router.get("/users/")
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    logger.info("Users retrieved")
    return users

@router.post("/portfolios/")
def create_portfolio(portfolio: PortfolioCreate, db: Session = Depends(get_db)):
    portfolio_date = date.fromisoformat(portfolio.date)
    new_portfolio = models.Portfolio(
        user_id=portfolio.user_id, 
        category=portfolio.category, 
        date=portfolio_date, 
        price=portfolio.price, 
        description=portfolio.description
    )
    db.add(new_portfolio)
    db.commit()
    db.refresh(new_portfolio)
    logger.info(f"Portfolio created: user_id={portfolio.user_id} category='{portfolio.category}' date='{portfolio.date}' price={portfolio.price}")
    return new_portfolio

@router.get("/portfolios/")
def read_portfolios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    portfolios = db.query(models.Portfolio).offset(skip).limit(limit).all()
    logger.info("Portfolios retrieved")
    return portfolios

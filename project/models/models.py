from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from database.connextion import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String, nullable=False)
    
    portfolios = relationship("Portfolio", back_populates="user")

class Portfolio(Base):
    __tablename__ = 'portfolios'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)
    
    user = relationship("User", back_populates="portfolios")

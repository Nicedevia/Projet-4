from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    
    id = Column(Integer, primary_key=True)
    email = Column(String(255))
    password = Column(String, nullable=False)
    
    portfolios = relationship("Portfolio", back_populates="user")
    
class Portfolio(Base):
    __tablename__ = 'portfolios'
    
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    category = Column(String, nullable=False)
    description = Column(String)
    date = Column(Date, nullable=False)
    price = Column(Float, nullable=False)
    
    ser = relationship("User", back_populates="portfolios")
    


engine = create_engine('sqlite:///portfolio.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(email='eli@ek.com', password='eli1234')
session.add(new_user)
session.commit()



new_portfolio = Portfolio(category='Investment', date='2023-06-25', user_id=new_user.id)
session.add(new_portfolio)
session.commit()




for user in session.query(User).all():
    print(user.email)
for portfolio in user.portfolios:
    print(portfolio.category, portfolio.date)

session.close()

    
    
    
    
    
    
    
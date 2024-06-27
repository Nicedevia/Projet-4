from pydantic import BaseModel

class PortfolioCreate(BaseModel):
    user_id: int
    category: str
    date: str
    price: float
    description: str = None

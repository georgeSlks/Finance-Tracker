from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    user_id: int
    category_id: int
    amount: float
    transaction_date: datetime
    description: str

class Transaction(BaseModel):
    id: int
    user_id: int
    category_id: int
    amount: float
    transaction_date: datetime
    description: str

    class Config:
        orm_mode = True

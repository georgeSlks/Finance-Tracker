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


'''

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE,
    amount NUMERIC(10,2) NOT NULL,
    transaction_date TIMESTAMP,
    description TEXT
);

'''
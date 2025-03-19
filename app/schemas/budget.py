from pydantic import BaseModel

class BudgetCreate(BaseModel):
    user_id: int
    category_id: int
    amount: float

class Budget(BaseModel):
    id: int
    user_id: int
    category_id: int
    amount: float

    class Config:
        orm_mode = True

'''
Use this query to create your budgets table:

CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE,
    amount NUMERIC(10,2) NOT NULL
);

'''
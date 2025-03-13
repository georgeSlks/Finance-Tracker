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

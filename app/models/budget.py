from app.db.database import database
from pydantic import BaseModel
from typing import List, Optional

class Budget(BaseModel):
    id: Optional[int]
    user_id: int
    category_id: int
    amount: float

# Function to fetch all budgets
async def get_all_budgets() -> List[Budget]:
    query = """
        SELECT id, user_id, category_id, amount
        FROM budgets;
    """
    result = await database.fetch_all(query)
    return [Budget(**row) for row in result]

# Function to fetch a single budget by ID
async def get_budget_by_id(budget_id: int) -> Optional[Budget]:
    query = """
        SELECT id, user_id, category_id, amount
        FROM budgets
        WHERE id = :budget_id;
    """
    result = await database.fetch_one(query, values={"budget_id": budget_id})
    return Budget(**result) if result else None

# Function to create a new budget
async def create_budget(budget: Budget) -> int:
    query = """
        INSERT INTO budgets (user_id, category_id, amount)
        VALUES (:user_id, :category_id, :amount)
        RETURNING id;
    """
    budget_id = await database.execute(query, values=budget.dict())
    return budget_id

# Function to update an existing budget
async def update_budget(budget_id: int, budget: Budget) -> bool:
    query = """
        UPDATE budgets
        SET user_id = :user_id, category_id = :category_id, amount = :amount
        WHERE id = :budget_id;
    """
    result = await database.execute(query, values={**budget.dict(), "budget_id": budget_id})
    return result > 0

# Function to delete a budget by ID
async def delete_budget(budget_id: int) -> bool:
    query = """
        DELETE FROM budgets
        WHERE id = :budget_id;
    """
    result = await database.execute(query, values={"budget_id": budget_id})
    return result > 0

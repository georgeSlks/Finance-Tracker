from fastapi import APIRouter, HTTPException, Depends
from app.db.database import get_db
import asyncpg

router = APIRouter()

# Create a new budget entry
@router.post("/budgets/")
async def create_budget(user_id: int, category_id: int, amount: float, db: asyncpg.Connection = Depends(get_db)):
    try:
        query = "INSERT INTO budgets (user_id, category_id, amount) VALUES ($1, $2, $3) RETURNING id"
        budget_id = await db.fetchval(query, user_id, category_id, amount)
        return {"message": "Budget created successfully", "budget_id": budget_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get a budget entry by ID
@router.get("/budgets/{budget_id}")
async def get_budget(budget_id: int, db: asyncpg.Connection = Depends(get_db)):
    budget = await db.fetchrow("SELECT * FROM budgets WHERE id = $1", budget_id)
    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")
    return dict(budget)

# Get all budgets for a user
@router.get("/budgets/user/{user_id}")
async def get_user_budgets(user_id: int, db: asyncpg.Connection = Depends(get_db)):
    budgets = await db.fetch("SELECT * FROM budgets WHERE user_id = $1", user_id)
    return [dict(budget) for budget in budgets]

# Delete a budget entry
@router.delete("/budgets/{budget_id}")
async def delete_budget(budget_id: int, db: asyncpg.Connection = Depends(get_db)):
    result = await db.execute("DELETE FROM budgets WHERE id = $1", budget_id)
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="Budget not found")
    return {"message": "Budget deleted successfully"}

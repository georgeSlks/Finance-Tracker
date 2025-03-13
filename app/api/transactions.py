from fastapi import APIRouter, HTTPException, Depends
from app.db.database import get_db
import asyncpg
from datetime import date

router = APIRouter()

# Create a new transaction
@router.post("/transactions/")
async def create_transaction(user_id: int, category_id: int, amount: float, transaction_date: date, description: str, db: asyncpg.Connection = Depends(get_db)):
    try:
        query = "INSERT INTO transactions (user_id, category_id, amount, transaction_date, description) VALUES ($1, $2, $3, $4, $5) RETURNING id"
        transaction_id = await db.fetchval(query, user_id, category_id, amount, transaction_date, description)
        return {"message": "Transaction created successfully", "transaction_id": transaction_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get a transaction by ID
@router.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: int, db: asyncpg.Connection = Depends(get_db)):
    transaction = await db.fetchrow("SELECT * FROM transactions WHERE id = $1", transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return dict(transaction)

# Get all transactions for a user
@router.get("/transactions/user/{user_id}")
async def get_user_transactions(user_id: int, db: asyncpg.Connection = Depends(get_db)):
    transactions = await db.fetch("SELECT * FROM transactions WHERE user_id = $1", user_id)
    return [dict(transaction) for transaction in transactions]

# Delete a transaction
@router.delete("/transactions/{transaction_id}")
async def delete_transaction(transaction_id: int, db: asyncpg.Connection = Depends(get_db)):
    result = await db.execute("DELETE FROM transactions WHERE id = $1", transaction_id)
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Transaction deleted successfully"}

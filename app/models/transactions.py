# app/models/transactions.py

from app.db.database import database
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Transaction(BaseModel):
    id: Optional[int]
    user_id: int
    category_id: int
    amount: float
    transaction_date: datetime
    description: Optional[str] = None

# Function to fetch all transactions
async def get_all_transactions() -> List[Transaction]:
    query = """
        SELECT id, user_id, category_id, amount, transaction_date, description
        FROM transactions;
    """
    result = await database.fetch_all(query)
    return [Transaction(**row) for row in result]

# Function to fetch a single transaction by ID
async def get_transaction_by_id(transaction_id: int) -> Optional[Transaction]:
    query = """
        SELECT id, user_id, category_id, amount, transaction_date, description
        FROM transactions
        WHERE id = :transaction_id;
    """
    result = await database.fetch_one(query, values={"transaction_id": transaction_id})
    return Transaction(**result) if result else None

# Function to create a new transaction
async def create_transaction(transaction: Transaction) -> int:
    query = """
        INSERT INTO transactions (user_id, category_id, amount, transaction_date, description)
        VALUES (:user_id, :category_id, :amount, :transaction_date, :description)
        RETURNING id;
    """
    transaction_id = await database.execute(query, values=transaction.dict())
    return transaction_id

# Function to update an existing transaction
async def update_transaction(transaction_id: int, transaction: Transaction) -> bool:
    query = """
        UPDATE transactions
        SET user_id = :user_id, category_id = :category_id, amount = :amount,
            transaction_date = :transaction_date, description = :description
        WHERE id = :transaction_id;
    """
    result = await database.execute(query, values={**transaction.dict(), "transaction_id": transaction_id})
    return result > 0

# Function to delete a transaction by ID
async def delete_transaction(transaction_id: int) -> bool:
    query = """
        DELETE FROM transactions
        WHERE id = :transaction_id;
    """
    result = await database.execute(query, values={"transaction_id": transaction_id})
    return result > 0

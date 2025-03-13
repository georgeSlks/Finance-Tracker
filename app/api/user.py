from fastapi import APIRouter, HTTPException, Depends
from app.db.database import get_db
import asyncpg

router = APIRouter()

# Create a new user
@router.post("/users/")
async def create_user(username: str, email: str, password: str, db: asyncpg.Connection = Depends(get_db)):
    try:
        query = "INSERT INTO users (username, email, password) VALUES ($1, $2, $3) RETURNING id"
        user_id = await db.fetchval(query, username, email, password)
        return {"message": "User created successfully", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get a user by ID
@router.get("/users/{user_id}")
async def get_user(user_id: int, db: asyncpg.Connection = Depends(get_db)):
    user = await db.fetchrow("SELECT id, username, email FROM users WHERE id = $1", user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return dict(user)

# Get all users
@router.get("/users/")
async def get_users(db: asyncpg.Connection = Depends(get_db)):
    users = await db.fetch("SELECT id, username, email FROM users")
    return [dict(user) for user in users]

# Delete a user
@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: asyncpg.Connection = Depends(get_db)):
    result = await db.execute("DELETE FROM users WHERE id = $1", user_id)
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

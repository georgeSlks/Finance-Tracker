from fastapi import APIRouter, HTTPException, Depends
from app.db.database import get_db
import asyncpg

router = APIRouter()

# Create a new category
@router.post("/categories/")
async def create_category(name: str, db: asyncpg.Connection = Depends(get_db)):
    try:
        query = "INSERT INTO categories (name) VALUES ($1) RETURNING id"
        category_id = await db.fetchval(query, name)
        return {"message": "Category created successfully", "category_id": category_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get a category by ID
@router.get("/categories/{category_id}")
async def get_category(category_id: int, db: asyncpg.Connection = Depends(get_db)):
    category = await db.fetchrow("SELECT * FROM categories WHERE id = $1", category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return dict(category)

# Get all categories
@router.get("/categories/")
async def get_categories(db: asyncpg.Connection = Depends(get_db)):
    categories = await db.fetch("SELECT * FROM categories")
    return [dict(category) for category in categories]

# Delete a category
@router.delete("/categories/{category_id}")
async def delete_category(category_id: int, db: asyncpg.Connection = Depends(get_db)):
    result = await db.execute("DELETE FROM categories WHERE id = $1", category_id)
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}

# app/models/categories.py

from app.db.database import database
from pydantic import BaseModel
from typing import List, Optional

class Category(BaseModel):
    id: Optional[int]
    name: str

# Function to fetch all categories
async def get_all_categories() -> List[Category]:
    query = """
        SELECT id, name
        FROM categories;
    """
    result = await database.fetch_all(query)
    return [Category(**row) for row in result]

# Function to fetch a single category by ID
async def get_category_by_id(category_id: int) -> Optional[Category]:
    query = """
        SELECT id, name
        FROM categories
        WHERE id = :category_id;
    """
    result = await database.fetch_one(query, values={"category_id": category_id})
    return Category(**result) if result else None

# Function to create a new category
async def create_category(category: Category) -> int:
    query = """
        INSERT INTO categories (name)
        VALUES (:name)
        RETURNING id;
    """
    category_id = await database.execute(query, values=category.dict())
    return category_id

# Function to update an existing category
async def update_category(category_id: int, category: Category) -> bool:
    query = """
        UPDATE categories
        SET name = :name
        WHERE id = :category_id;
    """
    result = await database.execute(query, values={**category.dict(), "category_id": category_id})
    return result > 0

# Function to delete a category by ID
async def delete_category(category_id: int) -> bool:
    query = """
        DELETE FROM categories
        WHERE id = :category_id;
    """
    result = await database.execute(query, values={"category_id": category_id})
    return result > 0

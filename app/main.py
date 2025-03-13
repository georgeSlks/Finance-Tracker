from fastapi import FastAPI
from app.api import user, transactions, budget, categories
from app.db.database import db  # Import the db instance from database.py
from app.core.config import settings

app = FastAPI()

# Include routers for different API endpoints
app.include_router(user.router, prefix="", tags=["users"])
app.include_router(transactions.router, prefix="", tags=["transactions"])
app.include_router(budget.router, prefix="", tags=["budgets"])
app.include_router(categories.router, prefix="", tags=["categories"])

# Database connection handling
@app.on_event("startup")
async def startup():
    # Establish the database connection pool on app startup
    await db.connect()
    print("Database connected.")

@app.on_event("shutdown")
async def shutdown():
    # Close the database connection pool when the app shuts down
    await db.disconnect()
    print("Database connection closed.")

import asyncpg
from app.core.config import settings

class Database:
    def __init__(self):
        self._pool = None

    async def connect(self):
        """Establish a connection pool to the PostgreSQL database."""
        self._pool = await asyncpg.create_pool(dsn=settings.DB_URL)

    async def disconnect(self):
        """Close the database connection pool."""
        if self._pool:
            await self._pool.close()

    async def fetch_one(self, query, *args):
        """Fetch a single record."""
        async with self._pool.acquire() as connection:
            return await connection.fetchrow(query, *args)

    async def fetch_all(self, query, *args):
        """Fetch multiple records."""
        async with self._pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def execute(self, query, *args):
        """Execute a query (INSERT, UPDATE, DELETE)."""
        async with self._pool.acquire() as connection:
            return await connection.execute(query, *args)

# Create a global database instance
db = Database()

# Dependency to get the database connection
async def get_db():
    """Returns a database connection."""
    if not db._pool:
        await db.connect()  # Connect if not already connected
    return db._pool

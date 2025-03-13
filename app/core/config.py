import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    DB_URL: str = os.getenv("DB_URL", f"postgresql://{DB_USER}:{DB_PASS}@localhost/finance_db")

settings = Settings()

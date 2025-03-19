from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


'''

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

'''
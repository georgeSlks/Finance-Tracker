from pydantic import BaseModel

class CategoryCreate(BaseModel):
    name: str

class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


'''
Use this query to create your categories table:

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

'''
# Finance-Tracker
This project is a Finance Management API built with FastAPI. It provides endpoints for managing users, transactions, budgets, and categories. 
The app integrates with a PostgreSQL database and offers a Swagger UI for interactive API testing.

# API Endpoints
The following are the API routes available in the app:

* <b> Users: </b>  
Create a new user: POST /users/  
Get all users: GET /users/  
Get a user by ID: GET /users/{user_id}  
Delete a user: DELETE /users/{user_id}  
* <b> Transactions: </b>  
Create a new transaction: POST /transactions/  
Get a transaction by ID: GET /transactions/{transaction_id}  
Get all transactions for a user: GET /transactions/user/{user_id}  
Delete a transaction: DELETE /transactions/{transaction_id}  
* <b> Budgets: </b>    
Create a new budget: POST /budgets/  
Get a budget by ID: GET /budgets/{budget_id}  
Get all budgets for a user: GET /budgets/user/{user_id}  
Delete a budget: DELETE /budgets/{budget_id}  
* <b> Categories: </b>  
Create a new category: POST /categories/  
Get a category by ID: GET /categories/{category_id}  
Get all categories: GET /categories/  
Delete a category: DELETE /categories/{category_id}  

# Technologies
* FastAPI: Python web framework for building APIs.
* PostgreSQL: Relational database for storing data.
* Pydantic: Python library for Data validation.
* Asyncpg: Python library For asynchronous queries.
* Swagger UI: Test the API endpoints directly from the Swagger UI interface.
* Uvicorn: The ASGI server that runs the FastAPI application.

# How to use it
* Inside /app create an .env file for your connection with postgresql. Add the below variable:
  ```sh
   DB_URL=postgresql://postgres_username:your_password@localhost/finance_db
   ```
* After creating your finance_db database create the tables.
* Run the application
  ```sh 
  uvicorn app.main:app --reload
  ```
* Access Swagger UI on:
  ```sh
  http://127.0.0.1:8000/docs
  ```
# Swagger UI Snapshots
![finance_tracker_swagger_ui_1](https://github.com/user-attachments/assets/48cf448a-d525-4639-8489-891962bd4c7f)  
![finance_tracker_swagger_ui_2](https://github.com/user-attachments/assets/a4ee6196-16de-4e76-8179-02d46b4b4f67)  

# Finance_db Tables
* <b> Users table </b>
![image](https://github.com/user-attachments/assets/e9fe05f8-41e3-4202-a1b4-c5bd0c144574)
* <b> Transactions Table </b>
![image](https://github.com/user-attachments/assets/b7dfb597-0fa4-4561-9949-0aeeb04af6e6)
* <b> Budgets Table </b>
![image](https://github.com/user-attachments/assets/e88cab75-7f42-44ac-8ca9-0e9e57482a90)
* <b> Categories Table </b>  
![image](https://github.com/user-attachments/assets/e748510c-e25f-42fa-bb31-0c46024b7f9e)

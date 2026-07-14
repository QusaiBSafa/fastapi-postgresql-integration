# FastAPI PostgreSQL Integration

## Description
This project is a simple FastAPI application integrated with PostgreSQL for basic CRUD operations.

## What's Built
- FastAPI backend
- PostgreSQL database integration
- Basic CRUD API for managing items

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-postgresql-integration.git
   cd fastapi-postgresql-integration
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   - Ensure PostgreSQL is running and create a database named `fastapi_db`.
5. Run the application:
   ```bash
   uvicorn src.main:app --reload
   ```

## API Documentation
- **GET /items/** - Retrieve all items
- **POST /items/** - Create a new item
- **GET /items/{item_id}** - Retrieve a specific item
- **PUT /items/{item_id}** - Update a specific item
- **DELETE /items/{item_id}** - Delete a specific item

## Environment Variables
- `DATABASE_URL` - PostgreSQL database URL (e.g., `postgresql://user:password@localhost/fastapi_db`)
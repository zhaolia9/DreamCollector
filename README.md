# Aurelia

Aurelia is a dream-and-poetry platform where users log dreams, tag symbols, and write poems inspired by those dreams.

## Tech
- Python
- MySQL
- Layered architecture (models, data access, app)

## Setup
1. Create DB:
   - Run `sql/01_create_tables.sql`
   - Run `sql/02_insert_test_data.sql`
2. Install deps:
   - `pip install -r backend/requirements.txt`
3. Run:
   - `python backend/app.py`

## Architecture
- models/ = domain objects
- data/ = repository / data access layer
- app.py = entry point (later becomes API)

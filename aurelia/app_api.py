# app_api.py
"""
Aurelia API - Service Layer + FastAPI

This file exposes CRUD endpoints for all entities:
- Users
- Dreams
- Symbols
- Poems
- DreamSymbols (many-to-many relationship)

Each endpoint calls the corresponding service method, which in turn
calls the business layer (UserBusiness, DreamBusiness, etc.)

Running Locally:
----------------
1. Ensure MySQL is running and environment variables set (or hardcode password for testing)
2. Install dependencies:
   pip install fastapi uvicorn mysql-connector-python pydantic
3. Run the server:
   uvicorn app_api:app --reload
4. Open Swagger UI at http://127.0.0.1:8000/docs

Hosting Options:
----------------
- Render.com / Railway.app: push repository, set environment variables, and run uvicorn with host 0.0.0.0 and $PORT
- Heroku: add MySQL add-on, use Procfile: "web: uvicorn app_api:app --host 0.0.0.0 --port $PORT"
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Import your service classes
from aurelia.app.services.user_service import UserManager
from aurelia.app.services.dream_service import DreamManager
from aurelia.app.services.symbol_service import SymbolManager
from aurelia.app.services.poem_service import PoemManager
from aurelia.app.services.dream_symbol_service import DreamSymbolManager

app = FastAPI(title="Aurelia Microservices API")

# Initialize services
# These service instances will be used to handle the business logic for each endpoint.
# had to update imports and class names to match the new structure, 
# but these should be the same as before
user_service = UserManager()
dream_service = DreamManager()
symbol_service = SymbolManager()
poem_service = PoemManager()
dream_symbol_service = DreamSymbolManager()

# ----------------------
# Pydantic Schemas -- These define the expected structure of request bodies for each endpoint.
# ----------------------
class UserSchema(BaseModel):
    name: str
    email: str

class DreamSchema(BaseModel):
    user_id: int
    title: str
    description: str
    date: str
    mood: str
    vividness: int

class SymbolSchema(BaseModel):
    name: str
    description: str

class PoemSchema(BaseModel):
    author_id: int
    dream_id: int
    content: str
    created_at: str

class DreamSymbolSchema(BaseModel):
    dream_id: int
    symbol_id: int

# ----------------------
# USERS Endpoints
# ----------------------
@app.post("/users")
def create_user(user: UserSchema):
    return user_service.create_user(user.name, user.email)
    # Pass fields directly to match UserManager signature.

@app.get("/users")
def get_all_users():
    return user_service.get_all_users() 
    # had to update method name since it's from the manager class
    # not the service class, but it should still work 
    # since the manager calls the service method internally

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return user_service.get_user_by_id(user_id)

@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserSchema):
    return user_service.update_user(user_id, user.name, user.email)

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return user_service.delete_user(user_id)

# ----------------------
# DREAMS Endpoints
# ----------------------
@app.post("/dreams")
def create_dream(dream: DreamSchema):
    return dream_service.create_dream(dream.user_id,
        dream.title,
        dream.description,
        dream.date,
        dream.mood,
        dream.vividness)

@app.get("/dreams")
def get_all_dreams():
    return dream_service.get_all_dreams()

@app.get("/dreams/{dream_id}")
def get_dream(dream_id: int):
    return dream_service.get_dream_by_id(dream_id,)

@app.put("/dreams/{dream_id}")
def update_dream(dream_id: int, dream: DreamSchema):
    return dream_service.update_dream(dream_id, 
        dream.user_id,
        dream.title,
        dream.description,
        dream.date,
        dream.mood,
        dream.vividness)

@app.delete("/dreams/{dream_id}")
def delete_dream(dream_id: int):
    return dream_service.delete_dream(dream_id)

# ----------------------
# SYMBOLS Endpoints
# ----------------------
@app.post("/symbols")
def create_symbol(symbol: SymbolSchema):
    return symbol_service.create_symbol(symbol.name, symbol.description)

@app.get("/symbols")
def get_all_symbols():
    return symbol_service.get_all_symbols()

@app.get("/symbols/{symbol_id}")
def get_symbol(symbol_id: int):
    return symbol_service.get_symbol_by_id(symbol_id)

@app.put("/symbols/{symbol_id}")
def update_symbol(symbol_id: int, symbol: SymbolSchema):
    return symbol_service.update_symbol(symbol_id, symbol.name, symbol.description)

@app.delete("/symbols/{symbol_id}")
def delete_symbol(symbol_id: int):
    return symbol_service.delete_symbol(symbol_id)

# ----------------------
# POEMS Endpoints
# ----------------------
@app.post("/poems")
def create_poem(poem: PoemSchema):
    return poem_service.create_poem(poem.author_id, poem.dream_id, poem.content)

@app.get("/poems")
def get_all_poems():
    return poem_service.get_all_poems()

@app.get("/poems/{poem_id}")
def get_poem(poem_id: int):
    return poem_service.get_poem_by_id(poem_id)

@app.put("/poems/{poem_id}")
def update_poem(poem_id: int, poem: PoemSchema):
    return poem_service.update_poem(poem_id, poem.author_id, poem.dream_id, poem.content)

@app.delete("/poems/{poem_id}")
def delete_poem(poem_id: int):
    return poem_service.delete_poem(poem_id)

# ----------------------
# DREAMSYMBOLS Endpoints
# ----------------------
# This endpoint creates a link between a dream and a symbol,
# allowing us to associate specific symbols with dreams in the database.
@app.post("/dreamsymbols")
def link_dream_symbol(link: DreamSymbolSchema):
    return dream_symbol_service.create_link_symbol_to_dream(link.dream_id, link.symbol_id)

@app.get("/dreamsymbols")
def get_all_dream_symbols(dream_id: Optional[int] = None):
    if dream_id:
        return dream_symbol_service.get_symbols_for_dream(dream_id)
    return dream_symbol_service.get_all_dream_symbols()

@app.get("/dreamsymbols/{link_id}")
def get_dream_symbol(link_id: int):
    return dream_symbol_service.get_symbols_for_dream(link_id)

@app.put("/dreamsymbols/{link_id}")
def update_dream_symbol(link_id: int, link: DreamSymbolSchema):
    return dream_symbol_service.update_link_symbol(link.dream_id, link.symbol_id)

@app.delete("/dreamsymbols")
def remove_dream_symbol(dream_id: int, symbol_id: int):
    return dream_symbol_service.delete_link_symbol_to_dream(dream_id, symbol_id)

if __name__ == "__main__":
    app.run(debug=False)
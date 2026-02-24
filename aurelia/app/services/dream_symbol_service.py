# app/services/dream_symbol_service.py

from fastapi import APIRouter
from aurelia.app.business.dream_symbol_manager import DreamSymbolManager

router = APIRouter()
manager = DreamSymbolManager()

# API endpoints for managing the relationship between dreams and symbols.

# This endpoint creates a link between a dream and a symbol, 
# allowing us to associate specific symbols with dreams in the database.
# renamed to create_link_symbol for clarity, but not currently used in the API
@router.post("/dreams/{dream_id}/symbols/{symbol_id}")
def create_link_symbol(dream_id: int, symbol_id: int):
    return manager.create_link_symbol_to_dream(dream_id, symbol_id) 

# This endpoint retrieves all symbols associated with a specific dream, 
# allowing us to see which symbols are linked to a given dream.
@router.get("/dreams/{dream_id}/symbols")
def get_symbols_for_dream(dream_id: int):
    return manager.get_symbols_for_dream(dream_id)

# This endpoint retrieves all dream-symbol links in the database, 
# allowing us to see all associations between dreams and symbols.
# added for completeness, but not currently used in the API
@router.get("/dreams-symbols")
def get_all_dream_symbols():
    return manager.get_all_dream_symbols()

# This endpoint updates an existing dream-symbol link with new information,
# allowing us to modify the association between a dream and a symbol in the database.
# added to generated code, named update_link_symbol for clarity, but not currently used in the API
@router.put("/dreams/{dream_id}/symbols/{symbol_id}")
def update_link_symbol(dream_id: int, symbol_id: int):
    return manager.update_link_symbol(dream_id, symbol_id)

# This endpoint removes the link between a dream and a symbol, 
# allowing us to disassociate a symbol from a dream in the database.
# renamed to delete_link_symbol for clarity, but not currently used in the API
@router.delete("/dreams/{dream_id}/symbols/{symbol_id}")
def delete_link_symbol(dream_id: int, symbol_id: int):
    return manager.delete_symbol_from_dream(dream_id, symbol_id) 
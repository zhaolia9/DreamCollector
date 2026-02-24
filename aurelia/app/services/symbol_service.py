# app/services/symbol_service.py

from fastapi import APIRouter
from aurelia.app.business.symbol_manager import SymbolManager

router = APIRouter()
manager = SymbolManager()

@router.post("/symbols")
def create_symbol(name: str, description: str):
    return manager.create_symbol(name, description)

@router.get("/symbols")
def get_symbols():
    return manager.get_all_symbols()

@router.get("/symbols/{symbol_id}")
def get_symbol(symbol_id: int):
    return manager.get_symbol_by_id(symbol_id)

@router.put("/symbols/{symbol_id}")
def update_symbol(symbol_id: int, name: str, description: str):
    return manager.update_symbol(symbol_id, name, description)

@router.delete("/symbols/{symbol_id}")
def delete_symbol(symbol_id: int):
    return manager.delete_symbol(symbol_id)
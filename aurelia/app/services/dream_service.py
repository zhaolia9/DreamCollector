# app/services/dream_service.py

from fastapi import APIRouter
from aurelia.app.business.dream_manager import DreamManager

router = APIRouter()
manager = DreamManager()

@router.post("/dreams")
def create_dream(user_id: int, title: str, description: str,
                 dream_date: str, mood: str, vividness: int):
    return manager.create_dream(user_id, title, description,
                                dream_date, mood, vividness)

@router.get("/dreams")
def get_dreams():
    return manager.get_all_dreams()

@router.get("/dreams/{dream_id}")
def get_dream(dream_id: int):
    return manager.get_dream_by_id(dream_id)

# This endpoint updates an existing dream with new information, 
# allowing us to modify the details of a dream in the database.
@router.put("/dreams/{dream_id}")
def update_dream(dream_id: int, user_id: int, title: str,
                 description: str, dream_date: str,
                 mood: str, vividness: int):
    return manager.update_dream(dream_id, user_id, title,
                                description, dream_date,
                                mood, vividness)

@router.delete("/dreams/{dream_id}")
def delete_dream(dream_id: int):
    return manager.delete_dream(dream_id)
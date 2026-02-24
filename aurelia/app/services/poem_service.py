# app/services/poem_service.py

from fastapi import APIRouter
from aurelia.app.business.poem_manager import PoemManager

router = APIRouter()
manager = PoemManager()

@router.post("/poems")
def create_poem(author_id: int, dream_id: int, content: str):
    return manager.create_poem(author_id, dream_id, content)

@router.get("/poems")
def get_poems():
    return manager.get_all_poems()

@router.get("/poems/{poem_id}")
def get_poem(poem_id: int):
    return manager.get_poem_by_id(poem_id)

@router.put("/poems/{poem_id}")
def update_poem(poem_id: int, author_id: int, dream_id: int, content: str):
    return manager.update_poem(poem_id, author_id, dream_id, content)

@router.delete("/poems/{poem_id}")
def delete_poem(poem_id: int):
    return manager.delete_poem(poem_id)
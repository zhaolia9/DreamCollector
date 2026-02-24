# app/services/user_service.py

from fastapi import APIRouter
from aurelia.app.business.user_manager import UserManager

router = APIRouter()
manager = UserManager()

@router.post("/users")
def create_user(name: str, email: str):
    return manager.create_user(name, email)

@router.get("/users")
def get_users():
    return manager.get_all_users()

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return manager.get_user_by_id(user_id)

@router.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str):
    return manager.update_user(user_id, name, email)

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return manager.delete_user(user_id)
# app/business/user_manager.py

from aurelia.app.data.data_provider import DataProvider
from aurelia.app.models.user import User
from types import SimpleNamespace

class UserManager:
    """
    Business layer for Users.
    Handles validation and domain rules before calling DataProvider.
    """

    def __init__(self):
        self.provider = DataProvider()

    # CREATE
    def create_user(self, name, email):
        user = SimpleNamespace(name=name, email=email)
        new_id = self.provider.create_user(user)
        return self.provider.read_user_by_id(new_id)

    # READ
    def get_user_by_id(self, user_id: int):
        return self.provider.read_user_by_id(user_id)

    def get_all_users(self):
        return self.provider.read_all_users()

    # UPDATE
    def update_user(self, user_id: int, name: str, email: str):
        return self.provider.update_user(User(user_id, name, email))

    # DELETE
    def delete_user(self, user_id: int):
        return self.provider.delete_user(user_id)
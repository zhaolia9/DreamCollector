# app/business/dream_manager.py

from aurelia.app.data.data_provider import DataProvider
from aurelia.app.models.dream import Dream
from datetime import date

class DreamManager:

    def __init__(self):
        self.provider = DataProvider()

# Business logic for managing dreams
# This class acts as an intermediary between the API layer and the data provider,
# allowing us to implement any necessary validation or processing before interacting with the database.
    def create_dream(self, user_id, title, description, dream_date, mood, vividness):
        if vividness < 1 or vividness > 10:
            raise ValueError("Vividness must be between 1 and 10.")
        return self.provider.create_dream(
            Dream(None, user_id, title, description, dream_date, mood, vividness)
        )

    def get_dream_by_id(self, dream_id):
        return self.provider.read_dream_by_id(dream_id)

    def get_all_dreams(self):
        return self.provider.read_all_dreams()

    def update_dream(self, dream_id, user_id, title, description, dream_date, mood, vividness):
        return self.provider.update_dream(
            Dream(dream_id, user_id, title, description, dream_date, mood, vividness)
        )

    def delete_dream(self, dream_id):
        return self.provider.delete_dream(dream_id)
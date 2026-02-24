# app/business/poem_manager.py

from aurelia.app.data.data_provider import DataProvider
from aurelia.app.models.poem import Poem
from datetime import datetime

class PoemManager:

    def __init__(self):
        self.provider = DataProvider()

    # Business logic for managing poems
    def create_poem(self, author_id, dream_id, content):
        return self.provider.create_poem(
            Poem(None, author_id, dream_id, content, datetime.now()) 
            # created_at is set to current time when poem is created
        )

    def get_poem_by_id(self, poem_id):
        return self.provider.read_poem_by_id(poem_id)

    def get_all_poems(self):
        return self.provider.read_all_poems()

    def update_poem(self, poem_id, author_id, dream_id, content):
        return self.provider.update_poem(
            Poem(poem_id, author_id, dream_id, content, datetime.now())
        )

    def delete_poem(self, poem_id):
        return self.provider.delete_poem(poem_id)
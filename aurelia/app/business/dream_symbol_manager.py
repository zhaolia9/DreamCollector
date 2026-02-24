# app/business/dream_symbol_manager.py

from aurelia.app.data.data_provider import DataProvider
from aurelia.app.models.dream_symbol import DreamSymbol

class DreamSymbolManager:
    """
    Business layer for many-to-many relationship.
    """

    def __init__(self):
        self.provider = DataProvider()

    # This method creates a link between a dream and a symbol in the database, 
    # allowing us to associate specific symbols with dreams.
    # renamed to create_link_symbol_to_dream for clarity, but not currently used in the API
    def create_link_symbol_to_dream(self, dream_id, symbol_id):
        return self.provider.create_dream_symbol(
            DreamSymbol(dream_id, symbol_id)
        )

    # This method retrieves all symbols associated with a specific dream, 
    # allowing us to see which symbols are linked to a given dream.
    def get_symbols_for_dream(self, dream_id):
        return self.provider.read_dream_symbols_by_dream(dream_id)

    # This method retrieves all dream-symbol links in the database, 
    # allowing us to see all associations between dreams and symbols.
    # added for completeness, but not currently used in the API
    def get_all_dream_symbols(self):
        return self.provider.read_all_dream_symbols()
    
    # This method updates the link between a dream and a symbol in the database,
    # allowing us to modify the association between a dream and a symbol.
    # added to generated code, named update_link_symbol for clarity, but not currently used in the API
    def update_link_symbol(self, dream_id, symbol_id):
        return self.provider.create_dream_symbol(
            DreamSymbol(dream_id, symbol_id)
        )
    
    # This method removes the link between a dream and a symbol in the database, 
    # allowing us to disassociate a symbol from a dream.
    # renamed to delete_link_symbol_to_dream for clarity, but not currently used in the API
    def delete_link_symbol_to_dream(self, dream_id, symbol_id): # added symbol_id parameter for deletion
        return self.provider.delete_dream_symbol(dream_id, symbol_id)